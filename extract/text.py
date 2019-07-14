from .bbox import bbox_from_node_attrs
from .positioned_node import PositionedNode
import copy


class Text(PositionedNode):
    """A class containing information from a <text> node"""

    def dump(self):
        return "<{} bbox=\"{}\">{}</{}>".format("text", self.dump_bbox_string(), self.contents, "text")

    def __init__(self, attr, contents):
        super().__init__(bbox_from_node_attrs(attr))
        self.attr = attr
        self.contents = contents

    def is_blank_node(self):
        return self.contents.strip() == ''


# XML text nodes only ever have one character
def get_text_from_xml_element(xml_element):
    text = xml_element.text
    if isinstance(text, str):
        text = text[0][0]
    else:
        text = ' '
    return Text(xml_element.attrib, text)


def text_attrs_styles_are_equal(attr1, attr2):
    attr1 = copy.copy(attr1)
    attr2 = copy.copy(attr2)

    if 'bbox' in attr1:
        del attr1['bbox']

    if 'bbox' in attr2:
        del attr2['bbox']

    if len(attr1.keys() - attr2.keys()) > 0:
        return False

    return list(attr1.values()) == list(attr2.values())
