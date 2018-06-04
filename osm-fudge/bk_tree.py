'''An implementation of bk-tree

More: https://en.wikipedia.org/wiki/BK-tree
'''

class BKTree:
    '''A bk-tree implementation and defined user methods
       for insertion and querying the string
    '''

    def __init__(self, root, distanceMetrics, options):
        self.tree = {root: {}}
        self.distanceMetrics = distanceMetrics
        self.options = options

    def insert(self, str1, subtree):
        self.__insert(str1, subtree)

    def __insert(self, str1, subtree):
        if not subtree or not subtree.keys() or len(subtree.keys()) == 0:
            return
        root = list(subtree.keys())[0]
        dist = self.distanceMetrics(root, str1, self.options)

        if dist in subtree[root]:
            self.insert(str1, subtree[root][dist])
        else:
            subtree[root][dist] = {str1: {}}

    def lookup(self, str1, subtree, tolerance, results):
        root = list(subtree.keys())[0]
        dist = self.distanceMetrics(root, str1, self.options)

        if dist <= tolerance:
            results.append(root)

        minimum = max([0, dist - tolerance])
        maximum = dist + tolerance

        for d in range(minimum, maximum + 1):
            if d in subtree[root]:
                self.lookup(str1, subtree[root][d], tolerance, results)
