class BinarySearchSymbolTable:
    def __init__(self, capacity):
        """
        use two arrays to track key-value pairs
        """
        self.values = [None]*capacity
        self.keys = [None]*capacity
        self.n = 0

    def get(self, key):
        if self.n == 0:
            return None

        i = self.rank(key)

        if i < self.n and self.keys[i] == key:
            return self.values[i]
        return None

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError
        return value

    def put(self, key, value):
        i = self.rank(key)
        if i < self.n and self.keys[i] == key:
            self.values[i] = value
            return

        for j in range(self.n-1, i, -1):
            self.keys[j] = self.keys[j-1]
            self.values[j] = self.values[j-1]

        self.keys[i] = key
        self.values[i] = value
        self.n += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def delete(self, key):
        i = self.rank(key)
        if i < self.n and self.keys[i] == key:
            for j in range(i,self.n-1):
                self.keys[j] = self.keys[j+1]
                self.values[j] = self.values[j+1]
            self.keys[self.n-1] = None
            self.values[self.n-1] = None
            self.n -= 1

    def __delitem__(self, key):
        self.delete(key)

    def size(self):
        return self.n

    def rank(self, key):
        """
        find number of keys that are smaller than the key
        """
        l, r = 0, self.n-1
        while l <= r:
            mid = l+ (r-l)//2
            if self.keys[mid] > key:
                r = mid - 1
            elif self.keys[mid] < key:
                l = mid + 1
            else:
                return mid
        return l

    def __iter__(self):
        return BinarySearchSymbolTable.Iterator(self.keys, self.values, self.n)

    class Iterator:
        def __init__(self, keys, values, n):
            self.keys = keys
            self.values = values
            self.n = n
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            self.index += 1
            if self.index == self.n:
                raise StopIteration

            return self.keys[self.index-1], self.values[self.index-1]

if __name__ == "__main__":
    st = BinarySearchSymbolTable(5)
    for i in range(5):
        st.put(i, i)

    assert st[0] == 0
    assert st[1] == 1

    count = 0
    for key, value in st:
        assert key == count
        assert value == count
        count += 1


    assert st.size() == 5
    for i in range(5):
        del st[i]
    assert st.size() == 0

