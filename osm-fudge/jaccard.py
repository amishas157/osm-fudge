'''Jaccard similarity function

Find jaccard distance between two given strings

More: https://en.wikipedia.org/wiki/Jaccard_index
'''

import sys
import n_gram

def find_jaccard_similarity(n, str1, str2):
    a = n_gram.find_n_grams(n, str1)
    b = n_gram.find_n_grams(n, str2)
    common = list(set(a) & set(b))
    union = list(set(a) | set(b))
    return len(common) / len(union)

if __name__ == "__main__":
    distance = find_jaccard_similarity(int(sys.argv[1]), sys.argv[2], sys.argv[3])
    print(distance)