class PositionedNode(object):
    def __init__(self, bbox):
        self.bbox = bbox

    def __repr__(self):
        return ' bbox="{}"'.format(repr(self.bbox)) if self.bbox else ''

    def is_above(self, y):
        if not self.bbox:
            return False

        return self.bbox.upper_left_coordinate.y > y

    def width(self):
        return round(self.bbox.lower_right_coordinate.x - self.bbox.upper_left_coordinate.x, 3)

    def height(self):
        return round(self.bbox.lower_right_coordinate.y - self.bbox.upper_left_coordinate.y, 3)

    def space_left(self, min_x):
        return round(self.bbox.upper_left_coordinate.x - min_x, 3)

    def space_right(self, max_x):
        return round(max_x - self.bbox.lower_right_coordinate.x, 3)

    def is_center_x(self, min_x, max_x, tolerance_percent=None):
        space_left = self.space_left(min_x)
        space_right = self.space_right(max_x)

        if tolerance_percent and tolerance_percent > 0:
            if space_right == space_left:
                return True

            total = space_left + space_right

            diff = 0
            if space_right > space_left:
                diff = space_right - space_left

            if space_left > space_right:
                diff = space_left - space_right

            if (diff / total) * 100 < tolerance_percent:
                return True

            return False

        return self.space_left(min_x) == self.space_right(max_x)