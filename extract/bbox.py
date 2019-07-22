from .coordinate import Coordinate


class BBoxRequiresTwoCoordinates(Exception):
    pass


class BBox(object):
    """Represents a bounding box.
    x0: the distance from the left of the page to the left edge of the box.
    y0: the distance from the bottom of the page to the lower edge of the box.
    x1: the distance from the left of the page to the right edge of the box.
    y1: the distance from the bottom of the page to the upper edge of the box.
    """

    def __repr__(self):
        return '{},{},{},{}'.format(
            self.upper_left_coordinate.x if not None else '',
            self.upper_left_coordinate.y if not None else '',
            self.lower_right_coordinate.x if not None else '',
            self.lower_right_coordinate.y if not None else '',
        )

    def __init__(self, upper_left_coordinate=None, lower_right_coordinate=None):
        """Create a BBox from two coordinate pairs.
        Returns:
        BBox object
        """
        if not upper_left_coordinate or not lower_right_coordinate:
            raise BBoxRequiresTwoCoordinates

        self.upper_left_coordinate = upper_left_coordinate
        self.lower_right_coordinate = lower_right_coordinate


class InvalidBboxString(Exception):
    pass


def bbox_from_string(bbox_string):
    points = bbox_string.split(",")

    if len(points) is not 4:
        raise InvalidBboxString

    upper_left_coordinate = Coordinate(float(points[0]), float(points[1]))
    lower_right_coordinate = Coordinate(float(points[2]), float(points[3]))

    return BBox(upper_left_coordinate, lower_right_coordinate)