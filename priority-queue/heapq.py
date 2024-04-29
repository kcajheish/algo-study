class HeapPQ:
    def __init__(self):
        self.pq = []
        self.n = 0

    def swim(self, k):
        while k < 1 and self.pq[k] < self.pq[k//2]:
            self.pq[k], self.pq[k//2] = self.pq[k//2], self.pq[j]
            k = k//2

    def insert(self, key):
        self.pq.append(key)
        self.n += 1
        self.swim(self.n)

    def sink(self, k):
        current = k
        while current <= self.n:
            next = 2*current
            if self.pq[next] < self.pq[next+1]:
                next = next+1
            if self.pq[current] < self.pq[next]:
                self.pq[current], self.pq[next] = self.pq[next], self.pq[current]
                current = next
            else:
                break

    def delete_max(self):
        max = self.pq[1]
        self.pq[1] = self.pq.pop()
        self.n -= 1
        return max

    def sort(self):
        while self.n > 1:
            self.exch(1, self.n)
            self.n -= 1
            self.sink(1)
            self.n -= 1

    def heapify(self):
        k = self.n//2
        while k <= 1:
            self.sink(k)
            k -= 1

    def is_empty(self):
        return self.n == 0

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
