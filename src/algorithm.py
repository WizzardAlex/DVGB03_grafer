#!/usr/bin/env python3

import sys
import logging

log = logging.getLogger(__name__)

from math import inf

def warshall(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Warshall's
    algorithm.

    Pre: adjlist is not empty.
    '''
    matrix = adjlist.adjacency_matrix()
    n = adjlist.node_cardinality()
    for i in range(n):
        for y in range(n):
            if i == y :
                matrix[i][y] = True
            elif matrix[i][y] == inf:
                matrix[i][y] = False
            else:
                matrix[i][y] = True
    for i in range(n):
        for y in range(n):
            for x in range(n):
                matrix[y][x] = matrix[y][x] or ( matrix[y][i] and matrix[i][x])



    return matrix

def floyd(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Floyd's algorithm.

    Pre: adjlist is not empty.
    '''
    matrix = adjlist.adjacency_matrix()
    n = adjlist.node_cardinality()
    for i in range(n):
        for y in range(n):
            for x in range(n):
                if y == x:
                    matrix[y][x] = 0
                else:
                    matrix[y][x] = min(matrix[y][x] , ( matrix[y][i] + matrix[i][x]))

    return matrix

def dijkstra(adjlist, start_node):
    '''
    Returns the result of running Dijkstra's algorithm as two N-length lists:
    1) distance d: here, d[i] contains the minimal cost to go from the node
    named `start_node` to the i:th node in the adjacency list.
    2) edges e: here, e[i] contains the node name that the i:th node's shortest
    path originated from.

    If the index i refers to the start node, set the associated values to None.

    Pre: start_node is a member of adjlist.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 2
    b|* * 2
    c|* * *

    For start node "a", the expected output would then be:

    d: [ None, 1, 2]
    e: [ None, 'a', 'a' ]
    '''
    nodeList = adjlist.list_nodes()
    nodes= adjlist.node_cardinality()
    d = [inf]*nodes
    e = [None]*nodes
    visited = ['F']*nodes
    tmpNode = adjlist.get_node(start_node)
    for i in range(len(nodes)):
        if nodeList[i] == start_node:
            d[i] = 0
            visited[i] = 'T'
            nodeList.pop(i)



    return d, e

def prim(adjlist, start_node):
    '''
    Returns the result of running Prim's algorithm as two N-length lists:
    1) lowcost l: here, l[i] contains the weight of the cheapest edge to connect
    the i:th node to the minimal spanning tree that started at `start_node`.
    2) closest c: here, c[i] contains the node name that the i:th node's
    cheapest edge orignated from.

    If the index i refers to the start node, set the associated values to None.

    Pre: adjlist is setup as an undirected graph and start_node is a member.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 3
    b|1 * 1
    c|3 1 *

    For start node "a", the expected output would then be:

    l: [ None, 1, 1]
    c: [ None, 'a', 'b' ]
    '''
    log.info("TODO: prim()")
    l = []
    c = []
    return l, c

if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
