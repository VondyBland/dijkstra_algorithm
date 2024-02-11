import sys

from dijkstra_algorithm import Dijkstra


dijkstra = Dijkstra()

graph = {
    'A':{'B': 5, 'C':3},
    'B':{'D': 2,'E':7},
    'C':{'B': 1, 'D': 6},
    'D':{'E':2},
    'E':{}
}

start_point = 'A'

dijkstra.find_shortest_paths(graph,start_point)