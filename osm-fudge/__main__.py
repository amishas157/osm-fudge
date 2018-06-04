import bk_tree
import sys

import levenshtein
import jaccard

distance_metrics = {
	'levenshtein': levenshtein.find_levenshtein_distance,
	'jaccard': jaccard.find_jaccard_similarity
}

with open(sys.argv[1], 'r') as file:
	initial_word = file.readline()
	metrics = sys.argv[2]
	if metrics not in distance_metrics.keys():
		sys.exit("Allowed metrics are {metrics}".format(metrics=list(distance_metrics.keys())))
	options = {'n' : 2}
	tree_obj = bk_tree.BKTree(initial_word, distance_metrics[metrics], options)

	for line in file: 
		if len(line) > 1:
			tree_obj.insert(line.strip(), tree_obj.tree)

	results = []
	tree_obj.lookup('parking', tree_obj.tree, 8, results)

	print(results)