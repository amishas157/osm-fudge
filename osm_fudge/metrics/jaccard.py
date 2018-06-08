'''Jaccard similarity function

Find jaccard distance between two given strings

More: https://en.wikipedia.org/wiki/Jaccard_index
'''

import argparse
import n_gram

def find_jaccard_similarity(str1, str2, options):
    a = n_gram.find_n_grams(options['n'], str1)
    b = n_gram.find_n_grams(options['n'], str2)
    common = list(set(a) & set(b))
    union = list(set(a) | set(b))
    return round(((len(common) / len(union)) * 100))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Finds jaccard distance between n-grams of two given strings')
    parser.add_argument('--n', type=int, required=True, help='n in n-grams')
    parser.add_argument('--x', type=str, required=True, help='source string')
    parser.add_argument('--y', type=str, required=True, help='destination string')
    args = parser.parse_args()

    distance = find_jaccard_similarity(args.n, args.x, args.y)
    print(distance)