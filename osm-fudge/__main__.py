import bk_tree
import sys

file  = open(sys.argv[1], 'r')

initial_word = file.readline()
tree_obj = bk_tree.BKTree(initial_word)

for line in file: 
	if len(line) > 1:
		tree_obj.insert(line.strip(), tree_obj.tree)

results = []
tree_obj.lookup('parking', tree_obj.tree, 8, results)

print(results)