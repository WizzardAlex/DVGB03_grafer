#!/usr/bin/env python3

import sys
import logging
from adjlist import AdjacencyList, Edge

log = logging.getLogger(__name__)

from math import inf

def warshall(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Warshall's
    algorithm.

    Pre: adjlist is not empty.
    '''
    log.info("TODO: warshall()")
    return [[]]

def floyd(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Floyd's algorithm.

    Pre: adjlist is not empty.
    '''
    log.info("TODO: floyd()")
    return [[]]

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
    log.info("TODO: dijkstra()")
    d = []
    e = []
    return d, e

def are_unconnected(adjlist, connected):
    # returns True if there are nodes in connected whose edges point to nodes not in connected
    nod = adjlist
    while not nod.is_empty():
        if nod.name() in connected:
            edg = nod.edges()
            while not edg.is_empty():
                if not edg.dst() in connected and edg.dst() != nod.name():
                    return True
                edg = edg.tail()
        nod = nod.tail()

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
    #log.info("TODO: prim()")
    
    print("nEW")
    connected = [start_node]
    tree = AdjacencyList() # keeps track of added nodes
    tree.add_node(start_node)

    # create initial edge and node
    while are_unconnected(adjlist, connected):
        curr_edge = Edge(weight=inf) # will be overridden by first legible node
        nod = adjlist
        while not nod.is_empty(): # find currently node with shortest edge

            edg = nod.edges()
            while not edg.is_empty(): # find best edge in node
                if not edg.dst() in connected and edg.weight() < curr_edge.weight() and edg.dst() != nod.name():
                    # better edge found, saving
                    curr_node = nod
                    curr_edge = edg
                edg = edg.tail()
            
            nod = nod.tail()
        
        print("edge to {} with weight {} from {}".format(curr_edge.dst(), curr_edge.weight(), curr_node.name()))

        # shortest edge found, find the node in the parallell tre
        
        nud = tree
        while not nud.is_empty():
            if nud.name() == curr_node.name():
                nud.edges().add(curr_edge.dst(), curr_edge.weight())
            nud = nud.tail()

        tree.add_node(curr_edge.dst())
        # find corresponding node for undirectional edge
        """
        nad = tree
        while not nad.is_empty():
            if nad.name() == curr_edge.dst():
                nad.edges().add(curr_node.name(), curr_edge.weight())
            nad = nad.tail()
        """
        connected.append(curr_edge.dst())
        input()

        print(connected)
    print(connected)
    n = adjlist.node_cardinality()
    l = [inf]*n
    c = [None]*n 

    nodelist = adjlist.list_nodes()
    for index, item in enumerate(nodelist):
        if not item in connected:
            l[index] = inf
            c[index] = None
            continue
        elif item == start_node:
            l[index] = None
            c[index] = None
            continue
    nad = tree
    while not nad.is_empty():
        edg = nad.edges()
        while not edg.is_empty():
            l[nodelist.index(edg.dst())] = edg.weight()
            c[nodelist.index(edg.dst())] = nad.name()
            edg = edg.tail()
        nad = nad.tail()

    print("prim prom")
    print(l)
    print("--")
    print(c)
    return l, c

if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
