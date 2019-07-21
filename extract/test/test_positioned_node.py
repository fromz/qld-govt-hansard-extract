from extract.bbox import BBox
from extract.positioned_node import PositionedNode
from extract.coordinate import Coordinate
import unittest


class TestPositionedNode(unittest.TestCase):
    def setUp(self):
        self.positioned_node = PositionedNode(
            BBox(Coordinate(79.2, 793.923),
                 Coordinate(139.809, 807.518))
        )

    def test_is_above_true(self):
        self.assertTrue(self.positioned_node.is_above(770))

    def test_is_above_false(self):
        self.assertFalse(self.positioned_node.is_above(800))

    def test_width(self):
        self.assertEqual(60.609, self.positioned_node.width())

    def test_space_left(self):
        self.assertEqual(79.2, self.positioned_node.space_left(0))

    def test_space_right(self):
        self.assertEqual(760.191, self.positioned_node.space_right(900))

    def test_is_center_true(self):
        positioned_node = PositionedNode(
            BBox(Coordinate(218.4, 748.128),
                 Coordinate(379.764, 765.312))
        )

        self.assertTrue(positioned_node.is_center_x(73.794, 527.736, 10))