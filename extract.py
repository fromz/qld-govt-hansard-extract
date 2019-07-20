import sys
import argparse
import xml.etree.ElementTree as ET
from extract.page import get_page_from_xml_element


debug = False


def main():
    """Tool to parse XML fom the queensland government."""

    parser = argparse.ArgumentParser(description='Extract content')
    parser.add_argument(dest='path_to_xml', action='store', type=str)
    results = parser.parse_args()

    root = ET.parse(results.path_to_xml).getroot()
    pages = []
    xml_page_elements = root.findall('.//page')
    for xml_page_element in xml_page_elements:
        page = get_page_from_xml_element(xml_page_element)

        min_x = page.min_x_boundary()
        max_x = page.max_x_boundary()
        if debug:
            print("Min: {}, Max: {}".format(min_x, max_x))

        # Apply conditional attributes and remove unneeded nodes
        for text_box in page.text_boxes:
            for text_line in text_box:
                text_line.compact_texts()
                for i, text in enumerate(text_line.texts):
                    if text.is_blank_node() or text.contents.strip() == '':
                        del text_line.texts[i]

                    if int(text.space_left(min_x)) == 28:
                        text.flags.append('paragraph-start')

                    if text.is_center_x(min_x, max_x, 10): # is a header
                        text.flags.append('header')
                        if text.style and text.style.font == 'Arial-BoldMT':
                            text.flags.append('primary-header' if text.contents.isupper() else 'secondary-header')

                    if text.is_above(790): # delete headers
                        del text_line.texts[i]

        pages.append(page)

    # prepare for output
    for page in pages:

        for text in page.texts():
            print("{}{}".format(
                "{}: ".format(",".join(text.flags)) if len(text.flags) > 0 else "",
                text.contents
            ))

        # print(repr(page))


if __name__ == '__main__':
    sys.exit(main())

