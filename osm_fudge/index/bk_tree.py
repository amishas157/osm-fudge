'''An implementation of bk-tree

More: https://en.wikipedia.org/wiki/BK-tree
'''


class BKTree:
    '''A bk-tree implementation and defined user methods
       for insertion and querying the string
    '''

    def __init__(self, distanceMetrics):
        self.tree = {}
        self.distanceMetrics = distanceMetrics

    def insert(self, item):
        self.__insert(item, self.tree)

    def __insert(self, str1, subtree):
        if not subtree.keys() or len(subtree.keys()) == 0:
            self.tree = {str1: {}}
            return

        root = list(subtree.keys())[0]
        dist = self.distanceMetrics(root, str1)

        if dist in subtree[root]:
            self.__insert(str1, subtree[root][dist])
        else:
            subtree[root][dist] = {str1: {}}

    def lookup(self, item, max_distance=None):
        return self.__lookup(item, self.tree, max_distance)

    def __lookup(self, str1, subtree, tolerance):
        stack = []
        stack.append(subtree)

        while stack:
            element = stack.pop()
            for tree_string in element.keys():
                dist = self.distanceMetrics(tree_string, str1)

                if dist <= tolerance:
                    yield tree_string
                    minimum = max([0, dist - tolerance])
                    maximum = dist + tolerance

                    for d in range(minimum, maximum + 1):
                        if d in element[tree_string].keys():
                            stack.append(element[tree_string][d])
