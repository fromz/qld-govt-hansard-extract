from .positioned_node import PositionedNode


class TextBox(PositionedNode):
    """A class containing information from a <textline> node"""

    def __init__(self, bbox):
        super().__init__(bbox)
        self.text_lines = []

    def __repr__(self):
        c = ''
        for text_line in self.text_lines:
            c += repr(text_line)

        return "<textbox{}>{}</textbox>".format(
            super().__repr__(),
            c
        )

    def __iter__(self):
        return iter(self.text_lines)

    def add_text_line_child(self, text_line):
        self.text_lines.append(text_line)

    def contains_text_nodes(self):
        for text_line in self.text_lines:
            if len(text_line.texts) > 0:
                return True

        return False
