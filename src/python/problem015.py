# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem015.py
#
# Lattice paths
# =============
# Published on Friday, 19th April 2002, 06:00 pm
#
# Starting in the top left corner of a 22 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?


class Vertex(object):

    def __str__(self):
        return "Vertex(%s: %s)" % (self.name, self.value)
    __repr__ = __str__

    def __init__(self, name):
        self.name = name
        self.value = 0
        self.incoming_edges = set()
        self.outgoing_edges = set()

    def add_incoming_edge(self, w):
        self.incoming_edges.add(w)
        w.outgoing_edges.add(self)

    def add_outgoing_edge(self, w):
        self.outgoing_edges.add(w)
        w.incoming_edges.add(self)

    def remove_incoming_edge(self, w):
        self.incoming_edges.remove(w)
        w.outgoing_edges.remove(self)

    def remove_outgoing_edge(self, w):
        self.outgoing_edges.remove(w)
        w.incoming_edges.remove(self)


def initialize_graph(max_x, max_y):
    graph = {}
    for i in xrange(1, max_x+1):
        for j in xrange(1, max_y+1):
            graph[(i,j)] = Vertex((i,j))
    for i in xrange(1, max_x+1):
        for j in xrange(1, max_y+1):
            v = graph[(i,j)]
            if i < max_x:
                v.add_outgoing_edge(graph[(i+1,j)])
            if j < max_y:
                v.add_outgoing_edge(graph[(i,j+1)])
    return graph


def count_paths(graph, sink_x, sink_y, source_x, source_y):
    sink = graph[(sink_x,sink_y)]
    sink.value = 1
    ends = [sink]
    seen = set()
    while ends:
        v = ends.pop(0)
        for w in v.incoming_edges:
            if w not in seen:
                ends.append(w)
                seen.add(w)
        for w in v.outgoing_edges:
            v.value += w.value
        v.outgoing_edges.clear()
    return graph[(source_x, source_y)].value


def main():
    max_x, max_y = 21, 21 
    graph = initialize_graph(max_x, max_y)
    count = count_paths(graph, max_x, max_y, 1, 1)
    print "There are %d routes through a 20x20 grid." % (count,)


if __name__ == "__main__":
    main()
