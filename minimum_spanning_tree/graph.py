class EdgeWeightedGraph:
    def __init__(self, V):
        self.adj = [[] for _ in range(V)]
        self.edges = []
        self.V = V

    def add_edge(self, edge):
        u = edge.either()
        v = edge.other(u)
        self.adj[u].append(edge)
        self.adj[v].append(edge)
        self.edges.append(edge)

    def adj(self, v):
        return self.adj[v]

    def edges(self):
        return self.edges

    def V(self):
        return self.V
