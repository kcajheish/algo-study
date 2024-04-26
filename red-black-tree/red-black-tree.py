"""
left leaning red black tree
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
           h                 x
        redx  .  ->          .   red h
        """
        assert h.left.color == RED
        x = h.left
        h.left = x.right
        x.right = h
        h.color = RED
        x.color = BLACK
        return x

    def flip_colors(self, h):
        assert self.is_red(h) == False
        assert self.is_red(h.left) == True
        assert self.is_red(h.right) == True
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK


