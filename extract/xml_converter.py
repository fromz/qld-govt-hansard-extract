from extract.bbox import bbox_from_string
from extract.bbox_merge import bbox_merge
from extract.page import Page
from extract.text import Text
from extract.text_box import TextBox
from extract.text_line import TextLine
from extract.text_style import TextStyle


def get_page_from_xml_element(xml_element):
    page = Page(bbox_from_string(xml_element.attrib['bbox']))
    for text_box_node in xml_element.findall('./textbox'):
        page.text_boxes.append(get_text_box_from_xml_element(text_box_node))
    return page


def get_text_line_from_xml_element(xml_element):

    t = TextLine(bbox_from_string(xml_element.attrib['bbox']))

    for text_xml_element in xml_element.findall('./text'):
        if len(text_xml_element.attrib) == 0:
            continue

        t.texts.append(get_text_from_xml_element(text_xml_element))

    return t


def get_text_box_from_xml_element(xml_element):
    text_lines = []
    bboxes = []
    for text_line_node in xml_element.findall('./textline'):
        text_line = get_text_line_from_xml_element(text_line_node)
        text_lines.append(text_line)
        bboxes.append(text_line.bbox)

    t = TextBox(bbox_merge(bboxes))
    t.text_lines = text_lines

    return t


# XML text nodes only ever have one character
def get_text_from_xml_element(xml_element):
    text = xml_element.text
    if isinstance(text, str):
        text = text[0][0]
    else:
        text = ' '
    bbox = None
    if 'bbox' in xml_element.attrib:
        bbox = bbox_from_string(xml_element.attrib['bbox'])

    return Text(bbox, text, TextStyle(
        xml_element.attrib['font'],
        float(xml_element.attrib['size']),
        xml_element.attrib['colourspace'],
        xml_element.attrib['ncolour']
    ))
