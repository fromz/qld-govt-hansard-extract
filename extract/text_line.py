from .text import Text, get_text_from_xml_element, text_attrs_styles_are_equal
from .bbox_merge import bbox_merge
from .bbox import bbox_from_node_attrs
from .positioned_node import PositionedNode
import copy


class TextLine(PositionedNode):
    """A class containing information from a <textline> node"""

    def dump(self):
        c = ''
        for text in self.texts:
            c += text.dump()

        return "<{} bbox=\"{}\">{}</{}>".format("textline", self.dump_bbox_string(), c, "textline")

    def __init__(self, bbox):
        super().__init__(bbox)
        self.texts = []

    def __iter__(self):
        return iter(self.texts)

    """ compacts text nodes by their style attributes, merging their bboxes """
    def compact_texts(self):
        merged_texts = []
        bboxes = []
        merged_text = Text({}, '')
        for i, text in enumerate(self.texts):
            styles_are_equal = text_attrs_styles_are_equal(merged_text.attr, text.attr)
            is_last_iteration = i + 1 == len(self.texts)

            if is_last_iteration:
                bboxes.append(text.bbox)
                merged_text.contents += text.contents

            if styles_are_equal is False or is_last_iteration:
                # New style of text, finish up last iteration
                merged_text.bbox = bbox_merge(bboxes)
                merged_texts.append(merged_text)

                bboxes = [] # reset bboxes
                merged_text = Text(text.attr, '') # reset ctext

            bboxes.append(text.bbox)
            merged_text.contents += text.contents

        merged_texts.pop(0)

        self.texts = merged_texts


def get_text_line_from_xml_element(xml_element):
    t = TextLine(bbox_from_node_attrs(xml_element.attrib))

    for text_xml_element in xml_element.findall('./text'):
        if len(text_xml_element.attrib) == 0:
            continue

        t.texts.append(get_text_from_xml_element(text_xml_element))

    return t
