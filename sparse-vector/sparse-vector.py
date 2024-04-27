class SparseVector:
    def __init__(self):
        vector = dict()

    def put(self, i, x):
        self.vector[i] = x

    def get(self, i):
        return self.vecttor[i]

    def indices(self):
        return self.vector.keys()

    def dot(self, that):
        total = 0
        for i in self.indices():
            total += that[i] * self.get(i)
        return total
