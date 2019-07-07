from .bbox import bbox_from_node_attrs


class Text(object):
    """A class containing information from a <text> node"""
    def __init__(self, attr, contents):
        self.attr = attr
        self.contents = contents
        self.bbox = bbox_from_node_attrs(attr)

    def is_blank_node(self):
        return self.contents.strip() == ''


def get_text_from_xml_element(xml_element):
    return Text(xml_element.attrib, xml_element.text)


def text_attrs_styles_are_equal(attr1, attr2):
    if 'bbox' in attr1:
        del attr1['bbox']

    if 'bbox' in attr2:
        del attr2['bbox']

    if len(attr1.keys() - attr2.keys()) > 0:
        return False

    return list(attr1.values()) == list(attr2.values())
