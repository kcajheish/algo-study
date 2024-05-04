class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def either(self):
        return self.v

    def other(self, this):
        if this == self.u:
            return self.u
        return self.v

    def compare_to(self, edge):
        if self.weight == edge.weight:
            return 0
        elif self.weight > edge.weight:
            return 1
        else:
            return -1

