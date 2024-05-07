from collections import deque
from graph import EdgeWeightedGraph
from union_find import UnionFind
from heapq import heappush, heappop
class Kruskal:
    def __init__(self):
        self.queue = deque()

    def mst(self, graph: EdgeWeightedGraph):
        pq = []
        for edge in graph.edges():
            heappush(pq, edge, key=lambda edge: edge.weight)

        uf = UnionFind(graph.V())
        while pq and len(self.queue) < graph.V()-1:
            edge = heappop(pq)
            u = edge.either()
            v = edge.other(u)
            if not uf.same(u, v):
                uf.union(u, v)
                self.queue.append(edge)

    def edges(self):
        return self.queue

class LazyPrim:
    def mst(self, graph):
        pq = []
        mst = []
        marked = [False]*graph.V()

        self.visit(graph, 0)

        while pq:
            edge = heappop(pq)
            u = edge.either()
            v = edge.other(u)
            if marked[u] and marked[v]:
                continue
            mst.append(edge)
            if not marked[u]:
                self.visit(graph, u, marked)
            if not marked[v]:
                self.visit(graph, v, marked)
        return mst

    def visit(self, graph, u, marked, heap):
        marked[u] = True
        for edge in graph.adj(u):
            if not marked[edge.other(u)]:
                heappush(edge, key=lambda edge: edge.w)
