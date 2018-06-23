'''Levenshtein distance function

Find similarity two given strings using levenshtein distance

More: https://en.wikipedia.org/wiki/Levenshtein_distance
'''

import numpy as np
import argparse


def find_levenshtein_distance(str1, str2):
    '''Returns levenshtein distance between two strings

    Args:
      str1: The source string
      str2: The destination string

    Returns:
      The minimum number of single-character edits (insertions, deletions or substitutions)
      required source string to destination string
    '''

    m = len(str1)
    n = len(str2)

    d = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    for j in range(n):
        for i in range(m):
            if str1[i] == str2[j]:
                cost = 0
            else:
                cost = 1
            d[i+1][j+1] = min([d[i][j + 1] + 1, d[i+1][j] + 1, d[i][j] + cost])

    return(d[m][n])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Finds levenshtein distance between two given strings')
    parser.add_argument('--x', type=str, required=True, help='source string')
    parser.add_argument('--y', type=str, required=True, help='destination string')
    args = parser.parse_args()

    distance = find_levenshtein_distance(args.x, args.y)
    print(distance)
