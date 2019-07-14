class PositionedNode(object):
    def __init__(self, bbox):
        self.bbox = bbox

    def dump_bbox_string(self):
        if not self.bbox:
            return ''

        return self.bbox.__repr__()

    def is_above(self, y):
        if not self.bbox:
            return False

        return self.bbox.upper_left_coordinate.y > y

    def width(self):
        return round(self.bbox.lower_right_coordinate.x - self.bbox.upper_left_coordinate.x, 3)

    def space_left(self, min_x):
        return self.bbox.upper_left_coordinate.x - min_x

    def space_right(self, max_x):
        return max_x - self.bbox.lower_right_coordinate.x

    # def is_center_x(self, min_x, max_x):
    #     print(self.space_left(min_x))
    #     print(self.space_right(max_x))
    #     print(self.width())