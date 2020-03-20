# Code to implement a B-tree
# Programmed by Olac Fuentes and Diego Aguirre

import matplotlib.pyplot as plt

class BTreeNode:
    # Constructor
    def __init__(self, data, child=[], is_leaf=True, max_items=5):
        self.data = data
        self.child = child
        self.is_leaf = is_leaf
        self.max_items = max_items # max_items must be odd and greater or equal to 3

    def is_full(self):
        return len(self.data) >= self.max_items

class BTree:
    # Constructor
    def __init__(self, max_items=5):
        self.max_items = max_items # Maximum number of keys allowed in a node
        self.root = BTreeNode(data=[],max_items=max_items)

    def find_child(self, k, node=None):
        # Determines value of c, such that k must be in subtree node.child[c], if k is in the BTree
        if node is None:
            node = self.root
        for i in range(len(node.data)):
            if k < node.data[i]:
                return i
        return len(node.data)

    def insert_internal(self, i, node=None):
        if node is None:
            node = self.root
        # node cannot be Full
        if node.is_leaf:
            self.insert_leaf(i, node)
        else:
            k = self.find_child(i, node)
            if node.child[k].is_full():
                m, l, r = self.split(node.child[k])
                node.data.insert(k, m)
                node.child[k] = l
                node.child.insert(k + 1, r)
                k = self.find_child(i, node)
            self.insert_internal(i, node.child[k])

    def split(self, node=None):
        if node is None:
            node = self.root
        # print('Splitting')
        # PrintNode(T)
        mid = node.max_items // 2
        if node.is_leaf:
            left_child = BTreeNode(node.data[:mid], max_items=node.max_items)
            right_child = BTreeNode(node.data[mid + 1:], max_items=node.max_items)
        else:
            left_child = BTreeNode(node.data[:mid], node.child[:mid + 1], node.is_leaf, max_items=node.max_items)
            right_child = BTreeNode(node.data[mid + 1:], node.child[mid + 1:], node.is_leaf, max_items=node.max_items)
        return node.data[mid], left_child, right_child

    def insert_leaf(self, i, node=None):
        if node is None:
            node = self.root
        node.data.append(i)
        node.data.sort()

    def leaves(self, node=None):
        if node is None:
            node = self.root
        # Returns the leaves in a b-tree
        if node.is_leaf:
            return [node.data]
        s = []
        for c in node.child:
            s = s + self.leaves(c)
        return s

    def insert(self, i, node=None):
        if node is None:
            node = self.root
        if not node.is_full():
            self.insert_internal(i, node)
        else:
            m, l, r = self.split(node)
            node.data = [m]
            node.child = [l, r]
            node.is_leaf = False
            k = self.find_child(i, node)
            self.insert_internal(i, node.child[k])

    def height(self, node=None):
        if node is None:
            node = self.root
        if node.is_leaf:
            return 0
        return 1 + self.height(node.child[0])

    def find(self, k, node=None):
        if node is None:
            node = self.root
        # Returns node where k is, or None if k is not in the tree
        if k in node.data:
            return node
        if node.is_leaf:
            return None
        return self.find(k, node.child[self.find_child(k, node)])

    def _set_x(self, dx, node=None):
        if node is None:
            node = self.root
        # Finds x-coordinate to display each node in the tree
        if node.is_leaf:
            return
        else:
            for c in node.child:
                self._set_x(dx, c)
            d = (dx[node.child[0].data[0]] + dx[node.child[-1].data[0]] + 10 * len(node.child[-1].data)) / 2
            dx[node.data[0]] = d - 10 * len(node.data) / 2

    def _draw_btree(self, dx, y, y_inc, fs, ax, node=None):
        if node is None:
            node = self.root
        # Function to display b-tree to the screen
        # It works fine for trees with up to about 70 data
        xs = dx[node.data[0]]
        if node.is_leaf:
            for itm in node.data:
                ax.plot([xs, xs + 10, xs + 10, xs, xs], [y, y, y - 10, y - 10, y], linewidth=1, color='k')
                ax.text(xs + 5, y - 5, str(itm), ha="center", va="center", fontsize=fs)
                xs += 10
        else:
            for i in range(len(node.data)):
                xc = dx[node.child[i].data[0]] + 5 * len(node.child[i].data)
                ax.plot([xs, xs + 10, xs + 10, xs, xs], [y, y, y - 10, y - 10, y], linewidth=1, color='k')
                ax.text(xs + 5, y - 5, str(node.data[i]), ha="center", va="center", fontsize=fs)
                ax.plot([xs, xc], [y - 10, y - y_inc], linewidth=1, color='k')
                self._draw_btree(dx, y - y_inc, y_inc, fs, ax, node.child[i])
                xs += 10
            xc = dx[node.child[-1].data[0]] + 5 * len(node.child[-1].data)
            ax.plot([xs, xc], [y - 10, y - y_inc], linewidth=1, color='k')
            self._draw_btree(dx, y - y_inc, y_inc, fs, ax, node.child[-1])

    def draw(self):
        # Find x-coordinates of leaves
        ll = self.leaves()
        dx = {}
        d = 0
        for l in ll:
            dx[l[0]] = d
            d += 10 * (len(l) + 1)
            # Find x-coordinates of internal nodes
        self._set_x(dx)
        # plt.close('all')
        fig, ax = plt.subplots()
        self._draw_btree(dx, 0, 30, 12, ax)
        ax.set_aspect(1.0)
        ax.axis('off')
        plt.show()




