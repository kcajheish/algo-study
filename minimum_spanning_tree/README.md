In a undirected weighted graph, find a connected & acyclic tree that spans all vertices in the graph.
    - acyclic
        - tree without cycle
    - connected
        - Each node on the tree can visit all the other nodes on the tree
    - undirected
        - Edge of graph is bi-directional.
    - weighted
        -  Edge has weight.

Minimun spanning tree must be unique when in the tree
1. each edge has unique weight
2. all nodes are connected

A cut divides a graph into two sets. Cutting edges are the edges that connects one set of nodes to the other.

Use contradiction to prove cut property
- We have a cut. Among all crossing edges, e has minimum weight but it’s not in MST
- The edge f is in MSP
- However, we can replace f with e and have a smaller spanning tree.
- Contradiction

Greedy
- Steps
    - Make a cut with no black crossing edge
    - Find minimum weighted edge
    - Repeat until we have V-1 black crossing edge
        - Note that V is number of vertices a graph has
- Correctness
    - A cut have a black crossing edge in MST
    - With less than V-1 crossing edges, there must be a cut that that doesn’t have black crossing edge. Thus, also doesn’t get stuck

Variations in MST
- Weighted edge is not unique
    - The result is multiple minimum spanning tree.
- Graph is not connected
    - The result is minimum spanning forest.

Kruskal
- steps
    - sort edge by weight in ascending order
    - take next edges as MST unless it forms a cycle
- correctness
    - Assume that we already have a tree.
    - We add next minimum weight edge(v-w) to the tree
    - The rest of vertices in cut connects to v in the tree; There are no black crossing edge, and the weight of edges are higher.
    - We proves that kruskal is a special case of greedy MST in that
        - edges are sorted in ascending order.
- need to detect graph is acyclic
    - union find
        - efficient, need space V and time logN
        - how? if u, v are in the same union, then adding edge, u-v, will create cycle.
    - dfs
        - slow, needs time V+E
- design
    - use queue to store edges in MST
    - use priority queue to store the edges and find the next min weighted edge
        - pq has logN time and in place sort.
    - use union find to detect acyclic
- time complexity
    - ElogE
