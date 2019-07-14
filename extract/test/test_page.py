from extract.page import Page
from extract.text import Text
from extract.text_box import TextBox
from extract.text_line import TextLine
from extract.bbox import BBox
from extract.coordinate import Coordinate
import unittest

class TestPage(unittest.TestCase):
    def setUp(self):
        self.page = Page({})
        bbox = BBox(Coordinate(79.2,793.923), Coordinate(139.809,807.518))
        tl = TextLine(bbox)
        tl.texts.append(Text(bbox, 'test'))
        tb = TextBox()
        tb.text_lines.append(tl)
        self.page.text_boxes.append(tb)

        bbox = BBox(Coordinate(70,793.923), Coordinate(354.369,807.518))
        tl = TextLine(bbox)
        tl.texts.append(Text(bbox, 'test'))
        tb = TextBox()
        tb.text_lines.append(tl)
        self.page.text_boxes.append(tb)

        bbox = BBox(Coordinate(505.2,793.923), Coordinate(530.169,807.518))
        tl = TextLine(bbox)
        tl.texts.append(Text(bbox, 'test'))
        tb = TextBox()
        tb.text_lines.append(tl)
        self.page.text_boxes.append(tb)

    def test_min_x_boundary(self):
        self.assertEqual(70, self.page.min_x_boundary())

    def test_max_x_boundary(self):
        self.assertEqual(530.169, self.page.max_x_boundary())