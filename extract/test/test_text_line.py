from extract.bbox import BBox
import unittest

from extract.coordinate import Coordinate
from extract.text import Text
from extract.text_line import TextLine
from extract.text_style import TextStyle


class TestTextLineCompactTexts(unittest.TestCase):
    def setUp(self):
        text_line = TextLine(BBox(Coordinate(459.840,753.697), Coordinate(521.235,765.210)))
        text_line.texts.append(Text(
            BBox(Coordinate(459.840,753.697), Coordinate(462.075,765.210)),
            'I',
            TextStyle('Arial-BoldMT', 11.513, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(462.120,753.697), Coordinate(467.483,765.210)),
            'S',
            TextStyle('Arial-BoldMT', 11.513, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(467.402,753.697), Coordinate(472.765,765.210)),
            'S',
            TextStyle('Arial-BoldMT', 11.513, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(472.802,753.697), Coordinate(478.607,765.210)),
            'N',
            TextStyle('Arial-BoldMT', 11.513, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(478.562,753.697), Coordinate(480.797,765.210)),
            ' ',
            TextStyle('Arial-BoldMT', 11.513, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(480.840,754.107), Coordinate(485.310,765.082)),
            '1',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(485.278,754.107), Coordinate(489.748,765.082)),
            '3',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(489.716,754.107), Coordinate(494.186,765.082)),
            '2',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(494.154,754.107), Coordinate(498.624,765.082)),
            '2',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(498.600,754.107), Coordinate(501.277,765.082)),
            '-',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(501.240,754.107), Coordinate(505.710,765.082)),
            '0',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(505.678,754.107), Coordinate(510.148,765.082)),
            '3',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(510.116,754.107), Coordinate(514.586,765.082)),
            '3',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(514.554,754.107), Coordinate(519.024,765.082)),
            '0',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        text_line.texts.append(Text(
            BBox(Coordinate(519.000,754.107), Coordinate(521.235,765.082)),
            ' ',
            TextStyle('ArialMT', 10.975, 'ICCBased', '[0]')
        ))
        self.compacted_text_line = text_line
        self.compacted_text_line.compact_texts()

    def test_correct_number_of_texts(self):
        self.assertEqual(len(self.compacted_text_line.texts), 2)

    expected_values = [
        {
            'node': 0,
            'font': 'Arial-BoldMT',
            'size': 11.513,
            'upper_left_coordinate_x': 459.840,
            'upper_left_coordinate_y':  753.697,
            'lower_right_coordinate_x': 480.797,
            'lower_right_coordinate_y': 765.210,
            'contents': 'ISSN ',
        },
        {
            'node': 1,
            'font': 'ArialMT',
            'size': 10.975,
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
                text_node.style.font,
                nodes_expected_values['font'],
                "Node {}".format(nodes_expected_values['node'])
            )

    def test_text_nodes_font_sizes_are_retained(self):
        for nodes_expected_values in self.expected_values:
            text_node = self.compacted_text_line.texts[nodes_expected_values['node']]
            self.assertEqual(
                text_node.style.font_size,
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