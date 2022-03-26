
from .EdgeType import EdgeType
from .Piece import Piece

class Edge:
    def __init__(self, type:EdgeType, parent: Piece):
        self.edgeType = type
        self.parent = parent
        self.orientation = None