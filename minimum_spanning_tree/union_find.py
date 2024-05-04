class UnionFind:
    def __init__(self, N):
        self.group = [i for i in range(N)]
        self.size = [1 for _ in range(N)]

    def find(self, x):
        p = self.group[x]
        if p != x:
            p = self.find(p)
            self.group[x] = p
        return p

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.size[y] < self.size[x]:
            x, y = y, x
        self.group[x] = y
        self.size[y] += self.size[x]
