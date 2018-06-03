'''N-gram function

Find similarity two given strings using n-gram mapping

More: https://en.wikipedia.org/wiki/N-gram
'''

import sys

def find_n_gram_matches(n, str1, str2):
    '''Returns number of n-gram matches between two strings

    Args:
      str1: The source string
      str2: The destination string

    Returns:
      The number of n-gram matches between source and destination string
    '''

    a = [str1[i:i+n] for i in range(len(str1) - (n-1))]
    b = [str2[i:i+n] for i in range(len(str2) - (n-1))]
    common = list(set(a) & set(b))
    matches = [min(str1.count(x) , str2.count(x)) for x in common]
    return sum(matches)


if __name__ == "__main__":
    matches = find_n_gram_matches(int(sys.argv[1]), sys.argv[2], sys.argv[3])
    print(matches)