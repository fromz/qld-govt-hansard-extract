from extract.text_line import get_text_line_from_xml_element
from extract.bbox import BBox
import xml.etree.ElementTree as ET
import unittest

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


class TestTextLineCompactTexts(unittest.TestCase):
    def setUp(self):
        # todo build a text_line object manually so there is no dependency on get_text_line_from_xml_element
        self.compacted_text_line = get_text_line_from_xml_element(ET.fromstring(s))
        self.compacted_text_line.compact_texts()

    def test_correct_number_of_texts(self):
        self.assertEqual(len(self.compacted_text_line.texts), 2)

    expected_values = [
        {
            'node': 0,
            'font': 'Arial-BoldMT',
            'size': '11.513',
            'upper_left_coordinate_x': 459.840,
            'upper_left_coordinate_y':  753.697,
            'lower_right_coordinate_x': 480.797,
            'lower_right_coordinate_y': 765.210,
            'contents': 'ISSN ',
        },
        {
            'node': 1,
            'font': 'ArialMT',
            'size': '10.975',
            'upper_left_coordinate_x': 480.840,
            'upper_left_coordinate_y':  754.107,
            'lower_right_coordinate_x': 521.235,
            'lower_right_coordinate_y': 765.082,
            'contents': '1322-0330 ',
        }
    ]

    def test_text_nodes_fonts_are_retained(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.attr['font'],
                nodes_expected_values['font'],
                "Node {}".format(nodes_expected_values['node'])
            )

    def test_text_nodes_font_sizes_are_retained(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.attr['size'],
                nodes_expected_values['size'],
                "Node {}".format(nodes_expected_values['node'])
            )

    def test_text_nodes_contents_are_merged(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.contents,
                nodes_expected_values['contents'],
                "Node {}".format(nodes_expected_values['node'])
            )

    def test_text_nodes_bboxes_are_merged_upper_left_x(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.bbox.upper_left_coordinate.x,
                nodes_expected_values['upper_left_coordinate_x'],
                "Node {}".format(nodes_expected_values['node'])
            )

    def test_text_nodes_bboxes_are_merged_upper_left_y(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.bbox.upper_left_coordinate.y,
                nodes_expected_values['upper_left_coordinate_y'],
                "Node {}".format(nodes_expected_values['node'])
            )

    def test_text_nodes_bboxes_are_merged_lower_right_x(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.bbox.lower_right_coordinate.x,
                nodes_expected_values['lower_right_coordinate_x'],
                "Node {}".format(nodes_expected_values['node'])
            )

    def test_text_nodes_bboxes_are_merged_lower_right_y(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.bbox.lower_right_coordinate.y,
                nodes_expected_values['lower_right_coordinate_y'],
                "Node {}".format(nodes_expected_values['node'])
            )