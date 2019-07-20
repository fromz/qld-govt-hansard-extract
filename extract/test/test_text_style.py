from extract.text_style import TextStyle
import unittest


class TestTextAttrsStylesAreEqual(unittest.TestCase):

    def test_text_attrs_styles_are_equal_true_when_same(self):
        self.assertTrue(TextStyle("ArialMT", "10.975", "ICCBased", "[0]")
                        .matches(TextStyle("ArialMT", "10.975", "ICCBased", "[0]")))

    def test_text_attrs_styles_are_equal_false_when_font_diff(self):
        self.assertFalse(TextStyle("ArialMTBold", "10.975", "ICCBased", "[0]")
                        .matches(TextStyle("ArialMT", "10.975", "ICCBased", "[0]")))

    def test_text_attrs_styles_are_equal_false_when_font_size_diff(self):
        self.assertFalse(TextStyle("ArialMT", "10.975", "ICCBased", "[0]")
                        .matches(TextStyle("ArialMT", "10.974", "ICCBased", "[0]")))