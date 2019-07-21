import sys
import argparse
import xml.etree.ElementTree as ET

from extract.xml_converter import get_page_from_xml_element


def main():
    """Tool to parse XML fom the queensland government."""

    parser = argparse.ArgumentParser(description='Extract content')
    parser.add_argument(dest='path_to_xml', action='store', type=str)
    parser.add_argument('--debug', action='store', type=bool)
    parser.add_argument('--out', action='store', type=str)
    flags = parser.parse_args()

    root = ET.parse(flags.path_to_xml).getroot()
    pages = []
    xml_page_elements = root.findall('.//page')
    for xml_page_element in xml_page_elements:
        page = get_page_from_xml_element(xml_page_element)

        min_x = page.min_x_boundary()
        max_x = page.max_x_boundary()
        if flags.debug:
            print("Min: {}, Max: {}".format(min_x, max_x))

        # Apply conditional attributes and remove unneeded nodes
        for text_box in page.text_boxes:
            for text_line in text_box:
                text_line.compact_texts()
                for i, text in enumerate(text_line.texts):
                    if text.is_blank_node() or text.contents.strip() == '':
                        del text_line.texts[i]

                    if int(text.space_left(min_x)) == 28:
                        text.flags.append('paragraph')

                    if text.is_center_x(min_x, max_x, 10): # is a header
                        text.flags.append('header')
                        if text.style and text.style.font == 'Arial-BoldMT':
                            text.flags.append('primary-header' if text.contents.isupper() else 'secondary-header')

                    if text.is_above(790): # delete headers
                        del text_line.texts[i]

        pages.append(page)

    # filter out blank text_boxes
    for page in pages:
        page.text_boxes = [text_box for text_box in page.text_boxes if text_box.contains_text_nodes()]

    # Need to sort texts by bbox I think. Sometimes they're out of order?

    # prepare for output
    for page in pages:
        if flags.debug:
            print(id(page), len(page.text_boxes))

        # mark paragraphs by their first flag - seems to work for paragraphs, is okay for now
        prev_typed_text_box = None
        unneeded_text_boxes = []
        for i, text_box in enumerate(page.text_boxes):
            first_text = next(iter(text_box.texts()), None)
            text_box.type = next(iter(first_text.flags), None)
            if text_box.type is not None:
                prev_typed_text_box = text_box


            if text_box.type == None:
                # Move all text_line nodes into it
                unneeded_text_lines = []
                for tli, text_line in enumerate(text_box.text_lines):
                    prev_typed_text_box.text_lines.append(text_line)
                    unneeded_text_lines.append(tli)

                for tli in sorted(unneeded_text_lines, reverse=True):
                    del page.text_boxes[i].text_lines[tli]

                if len(page.text_boxes[i].text_lines) == 0:
                    unneeded_text_boxes.append(i)

                page.text_boxes[i].bbox = page.text_boxes[i].merge_bboxes()

        for tbi in sorted(unneeded_text_boxes, reverse=True):
            del page.text_boxes[tbi]

        f = open("out.xml", "w+")
        f.write(repr(page))
        f.close()

        if flags.out == 'xml':
            print(repr(page))


if __name__ == '__main__':
    sys.exit(main())

