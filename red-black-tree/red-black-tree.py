"""
left leaning red black tree

We like to imitate 2-3 tree with a simple binary search tree.
1. A left leaning red link works as a glue for three node
2. No nodes has two red links connected to it.
    - 4-node is not valid in a 2-3 tree.
3. Every path from root to the null node has same number of black link.
    - 2-3 tree has perfect balance.



"""

"""
Use color to label a red/black link.
If a node has a red link connected from the parent, node color is Red
e.g. c.right.color = RED
    c
  /(red)
 d
"""
RED = True
BLACK = False

class Node:
    def __init__(self, key, val, color):
        self.val = val
        self.key = key
        self.left = None
        self.right = None
        self.color = None

class RedBlackTree:
    def __init__(self):
        root = None

    def get(self, key):
        """
        - same as BST but is usually faster due to perfectly balance.
        """
        node = self.root
        while node:
            if key > node.right.key:
                node = node.right
            elif key < node.left.key:
                node = node.left
            else:
                return node.val
        return None

    def put(self, h, key, val):
        if not h:
            return Node(key, val, RED)

        if key > h.key:
            h.right = self.put(h.right, key, val)
        elif key < h.key:
            h.left = self.put(h.left, key, val)
        else:
            h.val = val

        if self.is_red(h.right) and not self.is_red(h.left):
            self.rotate_left(h)

        if self.is_red(h.left) and self.is_red(h.left.left):
            self.rotate_right(h)

        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)

        return h

    def is_red(self, node):
        if not node:
            return False
        return node.color == RED

    def rotate_left(self, h):
        """
        - To make a right leaning red link to a left leaning one
        - The symmetric order and black balance is maintained
        - We didnt' change the height of black link
        - Node is still 2-3 node

        h                      x
        .  red x  ->       red h   .
        """
        assert h.right.color == RED
        x = h.right
        h.left = x.left
        x.left = h
        h.color = RED
        x.color = BLACK
        return x

    def rotate_right(self, h):
        """
        - To make a left leaning red link to a right leaning one
        - The symmetric order and black balance is maintained

           h                 x
        redx  .  ->          .   red h
        """
        assert h.left.color == RED
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def flip_colors(self, h):
        """
        - When both children has red link, flip the color and makes current node link red,
        """
        assert self.is_red(h) == False
        assert self.is_red(h.left) == True
        assert self.is_red(h.right) == True
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK


