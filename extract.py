import sys
import argparse
import xml.etree.ElementTree as ET
from extract.page import get_page_from_xml_element
from extract.bbox import BBox
from extract.coordinate import Coordinate

def main():
    """Tool to parse XML fom the queensland government."""

    parser = argparse.ArgumentParser(description='Extract content')
    parser.add_argument(dest='path_to_xml', action='store', type=str)
    results = parser.parse_args()

    header_area = BBox(Coordinate(0, 0), Coordinate(139, 841.920))

    root = ET.parse(results.path_to_xml).getroot()
    # todo: iterate by page, have some mechanism to identify text boxes based on positional details and/or style:
    #  - to ignore header and footer content
    #  - to identify headers
    xml_page_elements = root.findall('.//page')
    for xml_page_element in xml_page_elements:
        page = get_page_from_xml_element(xml_page_element)
        for text_box in page.text_boxes:

            for text_line in text_box:
                text_line.compact_texts()

                t = ''
                for text in text_line:
                    if text.is_above(790):
                        continue

                    if not text.is_blank_node():
                        t += text.contents

                if t.strip():
                    print(t)

        dump = page.dump()
        # print(dump)

if __name__ == '__main__':
    sys.exit(main())

