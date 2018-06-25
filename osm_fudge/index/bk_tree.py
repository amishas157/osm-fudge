'''An implementation of bk-tree

More: https://en.wikipedia.org/wiki/BK-tree
'''


def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)


class BKTree:
    '''A bk-tree implementation and defined user methods
       for insertion and querying the string
    '''

    def __init__(self, distanceMetrics):
        self.tree = [[]]
        self.distanceMetrics = distanceMetrics

    def insert_bk_element(self, level_index, str, dist):
        self.tree[level_index].append(dist)
        self.tree[level_index + 1].append(str)
        sibling_index = self.tree[level_index + 1].index(str)
        empty_child_index = level_index + (2 * (sibling_index + 1))
        self.append_empty_child(empty_child_index)

    def append_empty_child(self, index):
        self.tree.insert(index, [])
        self.tree.insert(index + 1, [])

    def insert(self, item):
        self.__insert(item, 0, 0)
        print(self.tree)

    def __insert(self, str1, level_index, sibling_index):
        if len(self.tree[0]) == 0:
            self.tree[0].append(str1)
            self.append_empty_child(1)
            return

        tree_element = self.tree[level_index][sibling_index]
        dist = self.distanceMetrics(tree_element, str1)

        for indexes, strings in grouped(self.tree[level_index + (2 * (sibling_index + 1)) - 1:], 2):
            if dist in indexes:
                self.__insert(str1, level_index + (2 * len(self.tree[level_index])), indexes.index(dist))
                break
            else:
                insert_index = level_index + (2 * (sibling_index + 1)) - 1
                self.insert_bk_element(insert_index, str1, dist)
                break

    def lookup(self, item, max_distance=None):
        return self.__lookup(item, max_distance)

    def __lookup(self, str1, tolerance):
        stack = []
        stack.append(self.tree)

        index = 0
        start = 0
        end = 0

        while stack:
            element = stack.pop()
            for i in range(start, end):
                tree_string = element[index][i]
                dist = self.distanceMetrics(tree_string, str1)

                if dist <= tolerance:
                    yield tree_string
                    minimum = max([0, dist - tolerance])
                    maximum = dist + tolerance

                    start = 0
                    end = len(element[index + 1] - 1)
                    index = index + (2 * len(element[index]))
                    stack.append(element)

            # for tree_string in element.keys():
            #     dist = self.distanceMetrics(tree_string, str1)

            #     if dist <= tolerance:
            #         yield tree_string
            #         minimum = max([0, dist - tolerance])
            #         maximum = dist + tolerance

            #         for d in range(minimum, maximum + 1):
            #             if d in element[tree_string].keys():
            #                 stack.append(element[tree_string][d])
