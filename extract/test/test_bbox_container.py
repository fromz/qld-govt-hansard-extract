from unittest import TestCase

from extract.bbox import BBox
from extract.positioned_node import PositionedNode
from extract.positioned_nodes import PositionedNodes
from extract.coordinate import Coordinate


class ChildClass(PositionedNodes):
    def __init__(self):
        super(ChildClass, self).__init__()
        self.my_child_nodes = [
            PositionedNode(BBox(Coordinate(0,0), Coordinate(1,1))),
            PositionedNode(BBox(Coordinate(0, 0), Coordinate(1, 1)))
        ]

    def positioned_nodes(self):
        return self.my_child_nodes


class TestBboxChildrenContainer(TestCase):

    def test_parent_class_uses_child_definition(self):
        child_class = ChildClass()
        self.assertEqual(child_class.positioned_notes_count(), 2)
