# Elementary Priority Queue

Priority Queue is a data structure that keeps order of items in some way.

For example, We want to keep track of max M items in a stream of N items. It can be implemented with stack or linked list. However, these approaches are really slow because we have to move everything larger to the right so the current item fit in the data structure.

In stack or linked list, items can be order or unordered, and their time complexity is N.
|         | ordered array   | unordered  array|
|---------|-----------------|-----------------|
| insert  | N               | 1               |
| findMax | 1               | N               |

Thus, a binary heap data structure comes into play. It can save time complexity to ~logN by keeping following variant:
1. It's balanced except the last level of nodes.
2. Parent's key is larger than child's key.

Binary heap can be implemented using array.
1. a[0] is empty
2. a[1] is the max element
3. If parent indice is k, left and right children are 2*k and 2k+1.
    - implication: move tree around by having arithmetic operation on the indice

Two possible violations to invariant. To fix these, either sink or swim the node.
1. Parent key becomes smaller than child's key.
2. Key becomes larger than parent's key.

API of binary heap pq
- delete_max()
- is_empty()
- sink(k)
- swim(k)
- insert(key)
