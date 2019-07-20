from .text import Text
from .bbox_merge import bbox_merge
from .bbox import bbox_from_string
from .positioned_node import PositionedNode
import copy


class TextLine(PositionedNode):
    """A class containing information from a <textline> node"""

    def __init__(self, bbox):
        super().__init__(bbox)
        self.texts = []

    def __repr__(self):
        c = ''
        for text in self.texts:
            c += repr(text)

        return "<{} bbox=\"{}\">{}</{}>".format("textline", self.dump_bbox_string(), c, "textline")

    def __iter__(self):
        return iter(self.texts)

    """ compacts text nodes by their style attributes, merging their bboxes """
    def compact_texts(self):
        all_texts = []

        texts = iter(self.texts)
        new_text = next(texts, None)
        
        while new_text:
            current_bboxes = []
            current_span_text = Text(copy.copy(new_text.bbox), '', copy.copy(new_text.style))
            current_span_text.contents = ''

            while new_text and current_span_text.style.matches(new_text.style):
                current_bboxes.append(new_text.bbox)
                current_span_text.contents += new_text.contents
                new_text = next(texts, None)
            else:
                # We've hit the end of the current span, so merge bboxes
                current_span_text.bbox = bbox_merge(current_bboxes)
                all_texts.append(current_span_text)

        self.texts = all_texts

