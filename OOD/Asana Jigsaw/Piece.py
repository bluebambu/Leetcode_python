
from .Edge import Edge
from .Orientation import Orientation

class Piece:
    def __init__(self, edges):
        self.edges = edges
        self.orientations = Orientation.values()
        self.ori_edge_map = {}

        for i, v in enumerate(self.orientations):
            self.ori_edge_map[v] = self.edges[i]
            self.edges[i].orientation = v

