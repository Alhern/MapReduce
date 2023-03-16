#!/usr/bin/env python3

import sys

sys.path.append('..')


def main():
    # Read the input from stdin and lowercase, strip, split each line
    for line in sys.stdin:
        words = line.lower().strip().split()
        # Each word is sorted, we print the sorted word and its original word
        for word in words:
            print(f'{"".join(sorted(word))}\t{word}')


if __name__ == "__main__":
    main()
