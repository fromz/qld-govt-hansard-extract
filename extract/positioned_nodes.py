class PositionedNodes(object):
    def __init__(self, positioned_nodes = []):
        self.pnodes = positioned_nodes

    def positioned_nodes(self):
        return self.pnodes

    def positioned_notes_count(self):
        return len(self.positioned_nodes())