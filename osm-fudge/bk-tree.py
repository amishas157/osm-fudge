'''An implementation of bk-tree

More: https://en.wikipedia.org/wiki/BK-tree
'''

import levenshtein

class BKTree:
    '''A bk-tree implementation and defined user methods
       for insertion and querying the string
    '''

    def __init__(self, root):
        self.tree = {root: {}}

    def insert(self, str1, subtree):
        root = list(subtree.keys())[0]
        dist = levenshtein.find_levenshtein_distance(root, str1)

        if (dist in subtree[root]):
            self.insert(str1, subtree[root][dist])
        else:
            subtree[root][dist] = {str1: {}}

    def lookup(self, str1, subtree, tolerance, results):
        root = list(subtree.keys())[0]
        dist = levenshtein.find_levenshtein_distance(root, str1)

        if (dist <= tolerance):
            results.append(root)

        minimum = max([0, dist - tolerance])
        maximum = dist + tolerance

        for d in range(minimum, maximum + 1):
            if (d in subtree[root]):
                self.lookup(str1, subtree[root][d], tolerance, results)
