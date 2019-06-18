class BBox(object):
    """Represents a bounding box."""

    def __init__(self, x0 = 0, y0 = 0, x1 = 0, y1 = 0):
        """Create a BBox from two coordinate pairs.

        Keyword arguments:
        x0, y0 -- Coordinates for the first point.
        x1, y1 -- Coordinates for the second point.

        All coordinates are cast to floats, which potentially introduces a loss of precision.
        TODO: investigate whether it would make more sense to use decimal.Decimal to preserve precision

        Returns:
        BBox object

        This docstring is based on (PEP-257)[https://www.python.org/dev/peps/pep-0257/].

        Curious about what a docstring is for? Try this:

        $ python
        Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
        [GCC 8.3.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import extract.bbox
        >>> help(extract.bbox.BBox)
        >>> help(extract.bbox.BBoxMixin)
        """
        self.x0 = float(x0)
        self.y0 = float(y0)
        self.x1 = float(x1)
        self.y1 = float(y1)


class BBoxMixin(object):
    """Mixin class for node types which contain a BBox.

    The coordinates for the bbox should be contained in
        self.attr['bbox']. The coordinates are assumed to be in the form
        of a comma-seperated string like so: "x0, y0, x1, y1"

    Adds a bbox() method which returns a BBox object."""

    def bbox(self):
        points = self.attr['bbox'].split(",")
        #box = BBox(points)
        #           ^^^^^^^
        # Creates a BBox object and passes a single argument, a list, which gets assigned to x0  
        box = BBox(*points)
        #          ^^^^^^^
        # Unpacks the list called points into its individual values, then passes these as individual
        # arguments into the constructor
        return box