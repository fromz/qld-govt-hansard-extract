class TextStyle(object):

    """A class containing information from a <page> node"""
    def __init__(self, font=None, font_size=None, colour_space=None, n_colour=None):
        self.font = font
        self.font_size = font_size
        self.colour_space = colour_space
        self.n_colour = n_colour

    def __repr__(self):
        attrs = []
        if self.font:
            attrs.append('font="{}"'.format(self.font))

        if self.font_size:
            attrs.append('font_size="{}"'.format(self.font_size))

        if self.colour_space:
            attrs.append('colour_space="{}"'.format(self.colour_space))

        if self.n_colour:
            attrs.append('n_colour="{}"'.format(self.n_colour))

        return " ".join(attrs)

    def matches(self, style):
        if style.font != self.font:
            return False

        if style.font_size != self.font_size:
            return False

        if style.colour_space != self.colour_space:
            return False

        if style.n_colour != self.n_colour:
            return False

        return True
