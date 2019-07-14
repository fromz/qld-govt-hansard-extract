class TextStyle():

    """A class containing information from a <page> node"""
    def __init__(self, font=None, font_size=None, colour_space=None, n_colour=None):
        self.font = font
        self.font_size = font_size
        self.colour_space = colour_space
        self.n_colour = n_colour

    def matches(self, style):
        if style.font is not self.font:
            return False

        if style.font_size is not self.font_size:
            return False

        if style.colour_space is not self.colour_space:
            return False

        if style.n_colour is not self.n_colour:
            return False

        return True
