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
        all_texts = []

        texts = iter(self.texts)
        new_text = next(texts)
        
        while new_text:
            current_bboxes = []
            current_span_text = Text(new_text.attr, '')
            
            while new_text and text_attrs_styles_are_equal(current_span_text.attr, new_text.attr):
                current_bboxes.append(new_text.bbox)
                current_span_text.contents += new_text.contents
                new_text = next(texts, None)
            else:
                # We've hit the end of the current span, so merge bboxes
                current_span_text.bbox = bbox_merge(current_bboxes)
                all_texts.append(current_span_text)

        self.texts = all_texts


def get_text_line_from_xml_element(xml_element):
    t = TextLine(bbox_from_node_attrs(xml_element.attrib))

    for text_xml_element in xml_element.findall('./text'):
        if len(text_xml_element.attrib) == 0:
            continue

        t.texts.append(get_text_from_xml_element(text_xml_element))

    return t
