import argparse
from functools import partial
import itertools
import sys

from osm_fudge.index import bk_tree
from osm_fudge.metrics import levenshtein
from osm_fudge.metrics import jaccard

distance_metrics = {
    'levenshtein': levenshtein.find_levenshtein_distance,
    'jaccard': jaccard.find_jaccard_similarity
}


def distance_metrics_method(metrics, options):
    if metrics == 'jaccard':
        return partial(distance_metrics[metrics], options=options)
    else:
        return distance_metrics[metrics]


def main():
    parser = argparse.ArgumentParser(description='Indexes OSM data in a bk-tree')
    parser.add_argument('--input', type=str, required=True, help='Input file for creating index')
    parser.add_argument('--metrics', type=str, choices=distance_metrics.keys(), required=True,
                        help='Input file for creating index')
    parser.add_argument('--max-distance', type=int, required=True,
                        help='Inter string distance allowed for potenital matches')
    parser.add_argument('--max-results', type=int, help='Maximum number of results required')
    parser.add_argument('--n-gram', type=int, help='n to be used for finding n-grams in jaccard similarity metrics')
    parser.add_argument('--query-strings', type=str, help='Comma delimited list of strings to be queried')
    args = parser.parse_args()
    with open(args.input, 'r') as file:
        metrics = args.metrics
        if args.n_gram:
            options = {'n': args.n_gram}
        tree_obj = bk_tree.BKTree(distance_metrics_method(metrics, options))

        for line in file:
            if len(line) > 1:
                tree_obj.insert(line.strip())

        if tree_obj.root is None:
            sys.exit("Error: Empty input file")

        tree_obj.freeze()
        if args.query_strings:
            for query_string in args.query_strings.split(','):
                gen = tree_obj.nearest(query_string.strip(), max_distance=args.max_distance)
                print('The results for query', query_string)
                if args.max_results:
                    print(list(itertools.islice(gen, args.max_results)))
                else:
                    print(list(gen))


if __name__ == "__main__":
    main()
