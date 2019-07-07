from unittest import TestCase
from extract.positioned_node import PositionedNode
from extract.bbox import BBox
from extract.coordinate import Coordinate

class TestPositionedNode(TestCase):
    def test_fits_in(self):
        positioned_node = PositionedNode(BBox(Coordinate(1,1), Coordinate(2,2)))
        self.assertTrue(positioned_node.fits_in(BBox(Coordinate(0.000,0.000), Coordinate(595.320,841.920))))


    def test_fits_in_negative(self):
        positioned_node = PositionedNode(BBox(Coordinate(1,1), Coordinate(4,4)))
        self.assertFalse(positioned_node.fits_in(BBox(Coordinate(0,0), Coordinate(3,3))))
