'''N-gram function

Find n-grams of a given string

More: https://en.wikipedia.org/wiki/N-gram
'''

import argparse

def find_n_grams(n, str):
    return [str[i:i+n] for i in range(len(str) - (n-1))]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Finds n-gram of a given string')
    parser.add_argument('--n', type=int, required=True, help='n in n-gram')
    parser.add_argument('--input', type=str, required=True, help='string input')
    args = parser.parse_args()

    n_grams = find_n_grams(args.n, args.input)
    print(n_grams)
