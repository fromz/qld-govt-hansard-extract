from .positioned_node import PositionedNode
from .text_box import get_text_box_from_xml_element
from .bbox import bbox_from_string


class Page(PositionedNode):

    """A class containing information from a <page> node"""
    def __init__(self, bbox):
        super().__init__(bbox)
        self.text_boxes = []

    def __repr__(self) -> str:
        c = ''
        for text_box in self.text_boxes:
            c += repr(text_box)

        return "<{}>{}</{}>".format("page", c, "page")

    def texts(self):
        texts = []
        for text_box in self.text_boxes:
            for text_line in text_box.text_lines:
                for text in text_line:
                    texts.append(text)

        return texts

    def min_x_boundary(self):
        xs = []
        for text_box in self.text_boxes:
            for text_line in text_box:
                for text in text_line:
                    xs.append(text.bbox.upper_left_coordinate.x)

        return min(xs)

    def max_x_boundary(self):
        xs = []
        for text_box in self.text_boxes:
            for text_line in text_box:
                for text in text_line:
                    xs.append(text.bbox.lower_right_coordinate.x)

        return max(xs)

def get_page_from_xml_element(xml_element):
    page = Page(bbox_from_string(xml_element.attrib['bbox']))
    for text_box_node in xml_element.findall('./textbox'):
        page.text_boxes.append(get_text_box_from_xml_element(text_box_node))
    return page