from .positioned_node import PositionedNode
from .text_style import TextStyle


class Text(PositionedNode):
    """A class containing information from a <text> node"""

    def __repr__(self):
        return "<text {} {}{}>{}</text>".format(
            super().__repr__(),
            repr(self.style) if self.style else "",
            ' flags="{}"'.format(",".join(self.flags)) if len(self.flags) > 0 else "",
            self.contents,
        )

    def __init__(self, bbox, contents: str = '', style: TextStyle = None):
        super().__init__(bbox)
        self.contents = contents
        self.style = style
        self.flags = []

    def is_blank_node(self):
        return self.contents.strip() == ''
