from typing import Dict, List, Tuple
from .graph import Graph
from .vertex import Vertex

def shortest_path(graph_world: Graph, source: str, destinations: str) -> Graph:
    pass

def findroute(graph_world: Graph, sources: List[str], destinations: List[str]) -> Graph:
    """Generate a subgraf from graph_world that connects sources and destinations

    Args:
        graph_world (Graph): our graph world that consists of 2136 kanji
        sources (List[str]): easier kanjis, ex: [一, 九, 七, 二, 人 ]
        destinations (List[str]): more advance kanjis, ex: [纖, 羚, 翔, 飜, 聽, 脩]

    Returns:
        Graph: subgraf from graph_world
    """
    paths = []
    for s in sources:
        for d in destinations:
            curr_path = shortest_path(graph_world, s, d)
            paths += curr_path
            
    