from .vertex import Vertex
from typing import Dict, List, Tuple

class Graph:
    def __init__(self):
        self.vert_dict: Dict[str, Vertex] = {}
        self.num_vertices: int = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, v: Vertex):
        self.num_vertices += 1
        self.vert_dict[v.data] = v

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, v_from, v_to, cost = 0):
        if v_from not in self.vert_dict:
            self.add_vertex(v_from)
        if v_to not in self.vert_dict:
            self.add_vertex(v_to)

        self. \
            vert_dict[v_from]. \
            add_neighbor(self.vert_dict[v_to], cost)

        self.vert_dict[v_to].add_neighbor(self.vert_dict[v_from], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
