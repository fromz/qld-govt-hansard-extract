from .bbox import BBoxMixin


class Text(BBoxMixin, object):
    """A class containing information from a <text> node"""
    attr = {}

    contents = ''

    def __init__(self):
        self.attr = {}
        self.contents = ''


def get_text_from_xml_element(xml_element):
    t = Text()
    t.attr = xml_element.attrib
    t.contents = xml_element.text
    return t


def text_attrs_styles_are_equal(attr1, attr2):
    if 'bbox' in attr1:
        del attr1['bbox']

    if 'bbox' in attr2:
        del attr2['bbox']

    if len(attr1.keys() - attr2.keys()) > 0:
        return False

    return list(attr1.values()) == list(attr2.values())
