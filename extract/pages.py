from extract.positioned_nodes import PositionedNodes
from .positioned_node import PositionedNode


class Pages(PositionedNode, PositionedNodes):

    """A class containing information from a <page> node"""
    def __init__(self, bbox):
        super().__init__(bbox)
        self.pages = []

    def __repr__(self) -> str:
        c = ''
        for page in self.pages:
            c += repr(page)

        return "<pages {}>{}</pages>".format(super().__repr__(), c)

    def positioned_nodes(self):
        return self.pages