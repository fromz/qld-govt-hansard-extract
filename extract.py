import sys
import argparse
import xml.etree.ElementTree as ET
from extract.page import get_page_from_xml_element

def main():
    """Tool to parse XML fom the queensland government."""

    parser = argparse.ArgumentParser(description='Extract content')
    parser.add_argument(dest='path_to_xml', action='store', type=str)
    results = parser.parse_args()

    root = ET.parse(results.path_to_xml).getroot()
    # todo: iterate by page, have some mechanism to identify text boxes based on positional details and/or style:
    #  - to ignore header and footer content
    #  - to identify headers
    pages = []
    xml_page_elements = root.findall('.//page')
    for xml_page_element in xml_page_elements:
        page = get_page_from_xml_element(xml_page_element)

        min_x = page.min_x_boundary()
        max_x = page.max_x_boundary()
        print("Min: {}, Max: {}".format(min_x, max_x))

        for text_box in page.text_boxes:
            for text_line in text_box:
                text_line.compact_texts()
                for i, text in enumerate(text_line.texts):
                    if text.is_blank_node() or text.contents.strip() == '':
                        del text_line.texts[i]

                    if text.is_center_x(min_x, max_x, 10): # is a header
                        text.flags.append('header')
                        if text.style and text.style.font == 'Arial-BoldMT':
                            text.flags.append('primary-header' if text.contents.isupper() else 'secondary-header')

                    if text.is_above(790): # delete headers
                        del text_line.texts[i]

        pages.append(page)

    for page in pages:

        for text_box in page.text_boxes:
            for text_line in text_box:

                t = ''
                for text in text_line:
                    t += "{}{}".format(
                        ",".join(text.flags),
                        text.contents
                    )

                print(t)

        # print(repr(page))


if __name__ == '__main__':
    sys.exit(main())

