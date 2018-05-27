'''Levenshtein distance function

Find similarity two given strings using levenshtein distance

More: https://en.wikipedia.org/wiki/Levenshtein_distance
'''

import sys

def find_levenshtein_distance(str1, str2):
    '''Returns levenshtein distance between two strings

    Args:
      str1: The source string
      str2: The destination string

    Returns:
      The minimum number of single-character edits (insertions, deletions or substitutions)
      required source string to  destination string
    '''

    m = len(str1)
    n = len(str2)

    d = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i;
    for j in range(n + 1):
        d[0][j] = j;

    for j in range(n):
        for i in range(m):
            if str1[i] == str2[j]:
                cost = 0
            else:
                cost = 1
            d[i+1][j+1] = min([d[i][j+ 1] + 1, d[i+1][j] + 1, d[i][j] + cost])

    return(d[m][n])


if __name__ == "__main__":
    distance = find_levenshtein_distance(sys.argv[1], sys.argv[2])
    print(distance)
