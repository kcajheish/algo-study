# Sparse Vector

Imagine you have to multiply a 2D matrix with an array

```math
a[][] * b[] = c[]
```

When the dimension of a and b reaches thousands, we need million times of multiplication. That's a lot of work especially when a lot of entries are zero for most of the time. The time complexity of this algorithm is $N^2$.

We like to skip those entries whose value is zero. A hash table is used as a row in the matrix, and only remember the entry that is non-zero. Hash table is chosen because we don't care about the order of those entries but rather care about the value at the index. This will reduce time complexity from $N^2$ to $N$

```python
import random

N = 1000
a = [SparseVector() for _ in range(N)]
x = [random.randint(3, 1000) for _ in range(N)]
b = [None for _ in range(N)]

for i, vector in enumerate(a):
    b[i] = vector.dot(x)
```
