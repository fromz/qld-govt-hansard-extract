from unittest import TestCase

from extract.bbox import BBox
from extract.positioned_node import PositionedNode
from extract.positioned_nodes import PositionedNodes
from extract.coordinate import Coordinate


class ChildClass(PositionedNode, PositionedNodes):
    def __init__(self):
        super(ChildClass, self).__init__(BBox(Coordinate(466.681, 788.160), Coordinate(527.287, 70.755)))
        self.my_child_nodes = [
            PositionedNode(BBox(Coordinate(466.681, 770.160), Coordinate(472.219, 801.755))),
            PositionedNode(BBox(Coordinate(472.199, 771.160), Coordinate(477.736, 100.755))),
            PositionedNode(BBox(Coordinate(524.519, 788.160), Coordinate(527.287, 70.755))),
        ]

    def positioned_nodes(self):
        return self.my_child_nodes


class TestPositionedNodesAfterMerge(TestCase):

    def setUp(self) -> None:
        self.child_class = ChildClass()
        del self.child_class.my_child_nodes[0]
        self.child_class.bbox = self.child_class.merge_bboxes()

    def test_parent_class_uses_child_definition(self):
        self.assertEqual(self.child_class.positioned_notes_count(), 2)

    def test_upper_left_x(self):
        self.assertEqual(self.child_class.bbox.upper_left_coordinate.x, 472.199)

    def test_upper_left_y(self):
        self.assertEqual(self.child_class.bbox.upper_left_coordinate.y, 788.160)

    def test_lower_right_x(self):
        self.assertEqual(self.child_class.bbox.lower_right_coordinate.x, 527.287)

    def test_lower_right_y(self):
        self.assertEqual(self.child_class.bbox.lower_right_coordinate.y, 70.755)
