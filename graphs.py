"""
    Project: CSC-445 - Algorithms
    Author: Ryan Clendenning, Kamylo Ramirez

    This file contains the data structures
    for the Layer 2 & Layer 3 topologies.

"""

# imported libraries
import random


# define the Node class utilized in the Graph class
class Node(object):
    def __init__(self, name: int, data: str, weight: int):
        self.name = name
        self.data = data
        self.weight = weight
        self.neighbors = []
        self.visited = False
        self.initialized = False


# define the Graph class and its functions
class Graph(object):
    def __init__(self, node_num: int):
        self.node_num = node_num
        self.nodes = [Node(-1, '', 0) for _ in range(node_num)]

    # method for removing non-inserted Node locations
    def clean(self):
        for node in self.nodes:
            if node.initialized is False:
                self.nodes.remove(node)

    # method for inserting Nodes into the graph
    def insert_node(self, name: int, data: str, weight: int):
        self.nodes[name] = Node(name, data, weight)
        self.nodes[name].initialized = True

    # method for retrieving specific Nodes' neighbor(s)
    def get_node_neighbors(self, n: int, x=False):
        if x is False:
            return self.nodes[n].neighbors
        else:
            for m in self.nodes[n].neighbors:
                print(m.name)

    # method for linking two Nodes together
    def add_neighbor(self, n: int, m: int):
        if self.nodes[m] not in self.nodes[n].neighbors and self.nodes[n] not in self.nodes[m].neighbors:
            self.nodes[n].neighbors.append(self.nodes[m])
            self.nodes[m].neighbors.append(self.nodes[n])


# method for creating complete graphs for generic testing
def gen_complete_graph(num_node: int):
    graph = Graph(num_node)
    for i in range(num_node):
        graph.insert_node(i, str(i), random.randint(2, 7))
        if i != 0:
            for j in range(i):
                graph.add_neighbor(i, j)
    graph.clean()
    return graph


# method for creating & returning a graph based on a graph.csv file
def base_graph(file_name: str):
    with open(file_name, 'r') as file:
        nodes = file.read().split('\n')
    graph = Graph(len(nodes))
    for i in range(len(nodes)):
        n = nodes[i].split(', ')
        graph.insert_node(int(n[0]), n[1], int(n[2]))
    graph.clean()
    return graph
