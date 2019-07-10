from extract.bbox import bbox_from_string, InvalidBboxString
import unittest


class TestBboxParsesCorrectly(unittest.TestCase):
    def setUp(self):
        self.bbox = bbox_from_string('459.840,753.697,462.075,765.210')

    def test_upper_left_x(self):
        self.assertEqual(self.bbox.upper_left_coordinate.x, 459.84)

    def test_upper_left_y(self):
        self.assertEqual(self.bbox.upper_left_coordinate.y, 753.697)

    def test_lower_right_x(self):
        self.assertEqual(self.bbox.lower_right_coordinate.x, 462.075)

    def test_lower_right_y(self):
        self.assertEqual(self.bbox.lower_right_coordinate.y, 765.210)


class TestBboxFromStringRaisesErrorWhenInvalid(unittest.TestCase):
    def test_one_point(self):
        with self.assertRaises(InvalidBboxString):
            bbox_from_string('1')

    def test_two_points(self):
        with self.assertRaises(InvalidBboxString):
            bbox_from_string('1,2')

    def test_three_points(self):
        with self.assertRaises(InvalidBboxString):
            bbox_from_string('1,2,3')

    def test_five_points(self):
        with self.assertRaises(InvalidBboxString):
            bbox_from_string('1,2,3,4,5')