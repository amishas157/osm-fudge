'''An implementation of bk-tree

More: https://en.wikipedia.org/wiki/BK-tree
'''

from recordclass import recordclass
from bisect import bisect_left
from bisect import bisect_right

Node = recordclass('Node', ['value', 'edges', 'children'])


def binary_search(values, min_value, max_value, lo=0, hi=None):
    hi = (hi if hi is not None else len(values))
    pos = bisect_left(values, min_value, lo, hi)
    if pos == hi:
        return -1, -1
    else:
        minimum = pos

    lo = minimum
    pos = bisect_right(values, max_value, lo, hi)
    maximum = (pos if pos != hi else hi)

    return minimum, maximum


class BKTree:
    '''A bk-tree implementation and defined user methods
       for insertion and querying the string
    '''

    def __init__(self, distanceMetrics):
        self.distanceMetrics = distanceMetrics
        self.root = None
        self.sorted = False

    def __insert(self, node, value):
        dist = self.distanceMetrics(node.value, value)
        if dist in node.edges:
            self.__insert(node.children[node.edges.index(dist)], value)
        else:
            node.edges.append(dist)
            node.children.append(Node(value, [], []))

    def insert(self, value):
        if not self.root:
            self.root = Node(value, [], [])
        else:
            self.__insert(self.root, value)
        self.sorted = False

    def __sort(self, node):
        if len(node.edges):
            node.edges, node.children = (list(t) for t in zip(*sorted(zip(node.edges, node.children))))
            for child in node.children:
                self.__sort(child)
        return

    def freeze(self):
        self.__sort(self.root)
        self.sorted = True

    def nearest(self, value, max_distance=None):
        assert self.root

        stack = []
        stack.append(self.root)

        while stack:
            node = stack.pop()
            dist = self.distanceMetrics(value, node.value)

            if dist <= max_distance:
                yield node.value

            minimum = max([0, dist - max_distance])
            maximum = dist + max_distance

            if self.sorted:
                min_index, max_index = binary_search(node.edges, minimum, maximum, 0, len(node.edges))
                stack.extend(node.children[min_index:max_index])
            else:
                for index, edge in enumerate(node.edges):
                    if edge >= minimum and edge <= maximum:
                        stack.append(node.children[index])
