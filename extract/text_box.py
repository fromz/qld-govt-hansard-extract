from .text_line import get_text_line_from_xml_element


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


def get_text_box_from_xml_element(xml_element):
    t = TextBox()
    for text_line_node in xml_element.findall('./textline'):
        text_line = get_text_line_from_xml_element(text_line_node)
        t.add_text_line_child(text_line)

    return t
