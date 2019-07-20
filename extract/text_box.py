class TextBox:
    """A class containing information from a <textline> node"""

    def __init__(self):
        self.text_lines = []

    def __repr__(self):
        c = ''
        for text_line in self.text_lines:
            c += repr(text_line)

        return "<{}>{}</{}>".format("textbox", c, "textbox")

    def __iter__(self):
        return iter(self.text_lines)

    def add_text_line_child(self, text_line):
        self.text_lines.append(text_line)
