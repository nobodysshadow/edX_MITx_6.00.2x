# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:35:59 2018

@author: nobodysshadow
"""

'''
Consider our continuing problem of permutations of three students in a line.
Use the enumeration we established when adding the nodes to our graph.
That is,

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]
so that ABC is Node 0, BCA is Node 3, etc.

Using Depth First Search, and beginning at the listed source nodes, give the
first path found to the listed destination nodes. For the purpose of this
exercise, assume DFS prioritizes lower numbered nodes. For example, if Node 2
is connected to Nodes 3 and 4, the first path checked will be 23. Additionally,
DFS will never return to a node already in its path.

To denote a path, simply list the numbers of the nodes exactly as done in the
lecture.

Hint: Visual representation
You can never go wrong with drawing a picture of the problem. Here is one
possible visualization. The possible permutations are denoted in the graph
below. From each node, you can choose to go in either direction. In this
particular depth-first-search problem, you will choose the lower numbered node
over the higher numbered one, even if it will lead to a longer path from the
source to the destination.
'''



class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildStudentGraph():
    nodes = []
    nodes.append(Node("ABC"))  # nodes[0]
    nodes.append(Node("ACB"))  # nodes[1]
    nodes.append(Node("BAC"))  # nodes[2]
    nodes.append(Node("BCA"))  # nodes[3]
    nodes.append(Node("CAB"))  # nodes[4]
    nodes.append(Node("CBA"))  # nodes[5]
    g = Graph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
    g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
    g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
    g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))
    g.addEdge(Edge(g.getNode('BCA'), g.getNode('CBA')))
    return g


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes;
       path and shortest are lists of nodes
    Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath is not None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest


def shortestPath(graph, start, end, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)


def testSP(source, destination):
    g = buildStudentGraph()
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                      toPrint=False)
    if sp is not None:
        print('Shortest path from', source, 'to', destination,
              'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


print("Exercise 1: Source 0 (ABC) -> Destination 4 (CAB)")
testSP('ABC', 'CAB')
print("Exercise 2: Source 4 (CAB) -> Destination 1 (ACB)")
testSP('CAB', 'ACB')
print("Exercise 3: Source 1 (ACB) -> Destination 1 (ACB)")
testSP('ACB', 'ACB')
print("Exercise 4: Source 2 (BAC) -> Destination 4 (CAB)")
testSP('BAC', 'CAB')
print("Exercise 5: Source 2 (BAC) -> Destination 3 (BCA)")
testSP('BAC', 'BCA')
print("Exercise 6: Source 3 (BCA) -> Destination 1 (ACB)")
testSP('BCA', 'ACB')

