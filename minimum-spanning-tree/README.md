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
