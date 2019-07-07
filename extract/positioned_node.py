class PositionedNode(object):
    def __init__(self, bbox):
        self.bbox = bbox

    def fits_in(self, bbox):
        if self.bbox.upper_left_coordinate.x < bbox.upper_left_coordinate.x:
            return False

        if self.bbox.upper_left_coordinate.y < bbox.upper_left_coordinate.y:
            return False

        if self.bbox.lower_right_coordinate.x > bbox.lower_right_coordinate.x:
            return False

        if self.bbox.lower_right_coordinate.y > bbox.lower_right_coordinate.y:
            return False

        return True
