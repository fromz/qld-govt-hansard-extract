class Coordinate(object):
    """Represents x/y coordinates"""

    def __repr__(self):
        return '{},{}'.format(self.x,self.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y


def upper_left_most_coordinate(coordinates):
    ys = []
    xs = []
    for coord in coordinates:
        xs.append(coord.x)
        ys.append(coord.y)

    x = 0
    if len(xs) > 0:
        x = min(xs)

    y = 0
    if len(ys) > 0:
        y = max(ys)

    return Coordinate(x, y)


def lower_right_most_coordinate(coordinates):
    ys = []
    xs = []
    for coord in coordinates:
        xs.append(coord.x)
        ys.append(coord.y)

    x = 0
    if len(xs) > 0:
        x = max(xs)

    y = 0
    if len(ys) > 0:
        y = min(ys)

    return Coordinate(x, y)