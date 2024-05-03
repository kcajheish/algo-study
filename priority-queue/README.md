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

Other operation:
- We can also create heap from an array with random order by a bottom up approach. Start with rightmost node with leaf and sink down the node one by one.
- To sort the array, we use the approach similar to delete max except we don't null out the last element.

Compare
- Pro
    - heap sort is a in place sorting with logN time
        - merge sort is not in place
        - quick sort is quadratic time(n^2) in worst case
- Con
    - not stable
        - Memory references to parent and children are not close to each other. It may take many reads to reach all three in physical memory. The situation may become worse if memory is disbtributed. So most people choose merge sort for their stability.
