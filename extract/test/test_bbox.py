from extract.bbox import BBoxMixin


class TestBboxClass(BBoxMixin):
    """A test class to demonstrate BBoxFactoryMixin"""
    attr = {
        'bbox': '459.840,753.697,462.075,765.210'
    }


def test_bbox_mixin():
    t = TestBboxClass()
    bb = t.bbox()
    assert bb.x0 == 459.84
    assert bb.y0 == 753.697
    assert bb.x1 == 462.075
    assert bb.y1 == 765.21
