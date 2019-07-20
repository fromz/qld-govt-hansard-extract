from extract.text import get_text_from_xml_element
from extract.text_style import TextStyle
import xml.etree.ElementTree as ET
import unittest


class TestGetTextFromXmlElement(unittest.TestCase):
    def setUp(self):
        s = """
                <text font="ArialMT" bbox="519.000,754.107,521.235,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">Y</text>
        """
        self.text = get_text_from_xml_element(ET.fromstring(s))

    def test_contents_retained(self):
        self.assertEqual(self.text.contents, 'Y')

    def test_font_retained(self):
        self.assertEqual(self.text.style.font, 'ArialMT')

    def test_bbox_retained(self):
        self.assertEqual(self.text.dump_bbox_string(), '519.0,754.107,521.235,765.082')

    def test_colour_space_retained(self):
        self.assertEqual(self.text.style.colour_space, 'ICCBased')

    def test_size_retained(self):
        self.assertEqual(self.text.style.font_size, '10.975')


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