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
    n = adjlist.node_cardinality()
    matrix = [ [inf]*n for i in range(n) ]
    
    remaining = adjlist.list_nodes()
    remaining.remove(start_node)
    
    new_adjl = AdjacencyList()

    # create initial edge and node
    curr_edge = Edge(weight=inf) # will be overridden by first legible node
    while len(remaining) != 0: # continue till all nodes are connected
        nod = adjlist

        while not nod.is_empty(): # find currently node with shortest edge
            # check if edges contain remaning nodes
            in_arr = list(map(nod.edges().find_node, remaining))

            if True in in_arr:
                # find first edge with dst in remaining
                edg = nod.edges()
                while not edg.dst() in remaining and edg.dst() != nod.name():
                    edg = edg.tail()
            else:
                # node doesnt have any edges to nodes in remaining, go next
                continue
            while not edg.is_empty(): # find best edge in node
                if edg.dst() in remaining and edg.weight() < curr_edge.weight() and edg.dst() != nod.name():
                    curr_node = nod
                    curr_edge = edg
                edg = edg.tail()
            
            nod = nod.tail()
        
        # shortest edge found, adding new node to tree
        new_node = AdjacencyList(name=curr_node.name())
        new_edge = Edge(dst=curr_edge.dst(), weight=curr_edge.weight())
        new_node.edges().add(new_edge)
        new_adjl.add(new_node)
        remaining.remove(nod.name())
        
    l = []
    c = []
    return l, c

if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
