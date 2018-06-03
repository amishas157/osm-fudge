'''N-gram function

Find n-grams of a given string

More: https://en.wikipedia.org/wiki/N-gram
'''

import sys

def find_n_grams(n, str):
    return [str[i:i+n] for i in range(len(str) - (n-1))]

if __name__ == "__main__":
    n_grams = find_n_grams(int(sys.argv[1]), sys.argv[2])
    print(n_grams)
