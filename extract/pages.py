from extract.bbox import BBox
from extract.coordinate import Coordinate
from extract.page import Page
from extract.positioned_nodes import PositionedNodes

class Pages(PositionedNodes):

    """A class containing information from a <page> node"""
    def __init__(self):
        self.pages = []

    def __repr__(self) -> str:
        c = ''
        for page in self.pages:
            c += repr(page)

        return "<pages>{}</pages>".format(c)

    def positioned_nodes(self):
        return self.pages

    def merge(self) -> Page:
        lower_right_ys = []
        lower_right_xs = []
        for page in self.pages:
            lower_right_ys.append(page.bbox.lower_right_coordinate.y)
            lower_right_xs.append(page.bbox.lower_right_coordinate.x)

        merged_page = Page(BBox(Coordinate(0,0), Coordinate(max(lower_right_xs), sum(lower_right_ys))))

        lower_right_ys.reverse()

        lower_right_y_count = len(lower_right_ys) - 1
        for i, page in enumerate(self.pages):
            y_offset = sum(lower_right_ys[i:lower_right_y_count])
            for text_box in page.text_boxes:
                # Change y coordinates append the necessary y_offset post page-merge
                text_box.bbox.lower_right_coordinate.y = text_box.bbox.lower_right_coordinate.y + y_offset
                text_box.bbox.upper_left_coordinate.y = text_box.bbox.upper_left_coordinate.y + y_offset
                for text_line in text_box.text_lines:
                    text_line.bbox.lower_right_coordinate.y = text_line.bbox.lower_right_coordinate.y + y_offset
                    text_line.bbox.upper_left_coordinate.y = text_line.bbox.upper_left_coordinate.y + y_offset
                    for text in text_line.texts:
                        text.bbox.lower_right_coordinate.y = text.bbox.lower_right_coordinate.y + y_offset
                        text.bbox.upper_left_coordinate.y = text.bbox.upper_left_coordinate.y + y_offset

                merged_page.text_boxes.append(text_box)


        return merged_page
