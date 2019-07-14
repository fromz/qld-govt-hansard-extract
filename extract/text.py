from .bbox import bbox_from_string, BBox
from .positioned_node import PositionedNode
from .text_style import TextStyle


class Text(PositionedNode):
    """A class containing information from a <text> node"""

    def dump(self):
        return "<{} bbox=\"{}\">{}</{}>".format("text", self.dump_bbox_string(), self.contents, "text")

    def __init__(self, bbox, contents, style=None):
        super().__init__(bbox)
        self.contents = contents
        self.style = style

    def is_blank_node(self):
        return self.contents.strip() == ''


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

    #font = None, font_size = None, colour_space = None, n_colour = None
    return Text(bbox, text, TextStyle(
        xml_element.attrib['font'],
        xml_element.attrib['size'],
        xml_element.attrib['colourspace'],
        xml_element.attrib['ncolour']
    ))