from .bbox import bbox_from_node_attrs
from .positioned_node import PositionedNode
from .text_box import get_text_box_from_xml_element


class Page(PositionedNode):

    """A class containing information from a <page> node"""
    def __init__(self, attr):
        super().__init__(bbox_from_node_attrs(attr))
        self.text_boxes = []

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

    def dump(self) -> str:
        c = ''
        for text_box in self.text_boxes:
            c += text_box.dump()

        return "<{}>{}</{}>".format("page", c, "page")


def get_page_from_xml_element(xml_element):
    page = Page(xml_element.attrib)
    for text_box_node in xml_element.findall('./textbox'):
        page.text_boxes.append(get_text_box_from_xml_element(text_box_node))
    return page