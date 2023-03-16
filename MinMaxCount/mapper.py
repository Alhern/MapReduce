#!/usr/bin/env python3

import sys
import csv

sys.path.append('.')


def main():
    reader = csv.reader(sys.stdin)
    # we skip the header
    next(reader)
    for row in reader:
        age = row[1]
        income = row[2]
        print(f'{age}\t{income}')


if __name__ == "__main__":
    main()

