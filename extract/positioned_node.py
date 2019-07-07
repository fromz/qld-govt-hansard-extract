class PositionedNode(object):
    def __init__(self, bbox):
        self.bbox = bbox

    def fits_in(self):
        return True
