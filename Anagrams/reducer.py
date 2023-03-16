#!/usr/bin/env python3

import sys
from itertools import groupby

sys.path.append('..')


def main():
    # Read the output of mapper.py
    # and group the key (sorted word) - value (original word) pairs by sorted_word
    grouped = groupby(sys.stdin, key=lambda line: line.strip().split('\t')[0])

    # For each group, print sorted words' lists if they have more than 1 anagram
    for sorted_word, group in grouped:
        anagrams = [word.strip().split('\t')[1] for word in group]
        if len(anagrams) > 1:
            print(f'{sorted_word}:\t{anagrams}')


if __name__ == "__main__":
    main()
