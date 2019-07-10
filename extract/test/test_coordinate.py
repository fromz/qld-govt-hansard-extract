from extract.coordinate import Coordinate, upper_left_most_coordinate, lower_right_most_coordinate
import unittest


class TestUpperLeftMostCoordinate(unittest.TestCase):
    def setUp(self):
        coordinates = [
            Coordinate(466.681, 780.160),
            Coordinate(472.199, 781.160),
            Coordinate(524.519, 788.160),
        ]
        self.coord = upper_left_most_coordinate(coordinates)

    def test_x(self):
        self.assertEqual(self.coord.x, 466.681)

    def test_y(self):
        self.assertEqual(self.coord.y, 788.160)


class TestLowerRightMostCoordinate(unittest.TestCase):
    def setUp(self):
        coordinates = (
            Coordinate(472.219, 111.755),
            Coordinate(477.736, 222.755),
            Coordinate(527.287, 801.755),
        )
        self.coord = lower_right_most_coordinate(coordinates)

    def test_x(self):
        self.assertEqual(self.coord.x, 527.287)

    def test_y(self):
        self.assertEqual(self.coord.y, 111.755)
