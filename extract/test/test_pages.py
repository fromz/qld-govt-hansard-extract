from extract.pages import Pages
from extract.page import Page
from extract.text import Text
from extract.text_box import TextBox
from extract.text_line import TextLine
from extract.bbox import BBox
from extract.coordinate import Coordinate
import unittest


class TestPages(unittest.TestCase):
    def setUp(self):
        pages = Pages()

        page = Page(BBox(Coordinate(0,0), Coordinate(595.320,841.920)))
        bbox = BBox(Coordinate(79.2,793.923), Coordinate(139.809,807.518))
        tl = TextLine(bbox)
        tl.texts.append(Text(bbox, 'test'))
        tb = TextBox(bbox)
        tb.text_lines.append(tl)
        page.text_boxes.append(tb)
        pages.pages.append(page)

        page = Page(BBox(Coordinate(0,0), Coordinate(595.320,841.920)))
        bbox = BBox(Coordinate(79.2,793.923), Coordinate(139.809,807.518))
        tl = TextLine(bbox)
        tl.texts.append(Text(bbox, 'test'))
        tb = TextBox(bbox)
        tb.text_lines.append(tl)
        page.text_boxes.append(tb)
        pages.pages.append(page)

        page = Page(BBox(Coordinate(0,0), Coordinate(595.320,841.920)))
        bbox = BBox(Coordinate(79.2,793.923), Coordinate(139.809,807.518))
        tl = TextLine(bbox)
        tl.texts.append(Text(bbox, 'test'))
        tb = TextBox(bbox)
        tb.text_lines.append(tl)
        page.text_boxes.append(tb)
        pages.pages.append(page)

        self.page = pages.merge()

    def test_page_boundaries(self):
        self.assertEqual(595.32, self.page.bbox.lower_right_coordinate.x)
        self.assertEqual(2525.76, round(self.page.bbox.lower_right_coordinate.y, 3))
        self.assertEqual(3, len(self.page.texts()))