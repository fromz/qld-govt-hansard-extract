import xml.etree.ElementTree as ET
import unittest

from extract.bbox import BBox
from extract.coordinate import Coordinate
from extract.xml_converter import get_text_from_xml_element, get_text_line_from_xml_element


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
        self.assertIsInstance(self.text.bbox, BBox)
        self.assertIsInstance(self.text.bbox.lower_right_coordinate, Coordinate)
        self.assertIsInstance(self.text.bbox.upper_left_coordinate, Coordinate)
        self.assertEqual(repr(self.text.bbox), '519.0,754.107,521.235,765.082')

    def test_colour_space_retained(self):
        self.assertEqual(self.text.style.colour_space, 'ICCBased')

    def test_size_retained(self):
        self.assertEqual(self.text.style.font_size, 10.975)


s = """<textline bbox="459.840,753.697,521.235,765.210">
<text font="Arial-BoldMT" bbox="459.840,753.697,462.075,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">I</text>
<text font="Arial-BoldMT" bbox="462.120,753.697,467.483,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">S</text>
<text font="Arial-BoldMT" bbox="467.402,753.697,472.765,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">S</text>
<text font="Arial-BoldMT" bbox="472.802,753.697,478.607,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">N</text>
<text font="Arial-BoldMT" bbox="478.562,753.697,480.797,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513"> </text>
<text font="ArialMT" bbox="480.840,754.107,485.310,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">1</text>
<text font="ArialMT" bbox="485.278,754.107,489.748,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">3</text>
<text font="ArialMT" bbox="489.716,754.107,494.186,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">2</text>
<text font="ArialMT" bbox="494.154,754.107,498.624,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">2</text>
<text font="ArialMT" bbox="498.600,754.107,501.277,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">-</text>
<text font="ArialMT" bbox="501.240,754.107,505.710,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">0</text>
<text font="ArialMT" bbox="505.678,754.107,510.148,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">3</text>
<text font="ArialMT" bbox="510.116,754.107,514.586,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">3</text>
<text font="ArialMT" bbox="514.554,754.107,519.024,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">0</text>
<text font="ArialMT" bbox="519.000,754.107,521.235,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975"> </text>
<text>
</text>
</textline>"""


class TestGetTextLineFromXmlElement(unittest.TestCase):
    def setUp(self):
        self.text_line = get_text_line_from_xml_element(ET.fromstring(s))

    def test_correct_number_of_texts(self):
        self.assertEqual(len(self.text_line.texts), 15)

    def test_text_line_bbox_is_retained(self):
        self.assertIsInstance(self.text_line.bbox, BBox)
