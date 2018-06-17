import argparse
import sys
from functools import partial

from osm_fudge.index import bk_tree
from osm_fudge.metrics import levenshtein
from osm_fudge.metrics import jaccard

distance_metrics = {
	'levenshtein': levenshtein.find_levenshtein_distance,
	'jaccard': jaccard.find_jaccard_similarity
}

def main():
	parser = argparse.ArgumentParser(description='Indexes OSM data in a bk-tree')
	parser.add_argument('--input', type=str, required=True, help='Input file for creating index')
	parser.add_argument('--metrics', type=str, choices=distance_metrics.keys(), required=True, help='Input file for creating index')
	args = parser.parse_args()
	with open(args.input, 'r') as file:
		metrics = args.metrics
		options = {'n' : 2}
		tree_obj = bk_tree.BKTree(partial(distance_metrics[metrics], options=options))

		for line in file:
			if len(line) > 1:
				tree_obj.insert(line.strip())

		print(tree_obj.lookup('parking', 8))

if __name__ == "__main__":
	main()
