#!/usr/bin/env python3

import sys
from itertools import groupby

sys.path.append('.')


def main():
    last_age = None
    count = max_income = 0
    min_income = float('inf')  # need to use this otherwise the minimum will always be 0

    # Use the input from mapper.py to count the number of people of each age
    # and find the maximum and minimum income of each age.
    # We use then convert both age and salary as int & floats, we need this for calculations
    for line in sys.stdin:
        age, salary = line.strip().split('\t')
        age = int(age)
        salary = float(salary)

        # If age is different from the last age, we print the last age's min and max income
        if last_age and last_age != age:
            print(f'COUNT: {count} | AGE: {last_age} | MIN: {min_income} | MAX: {max_income}')
            last_age = age
            max_income = salary
            min_income = salary
            count = 1
        else:
            last_age = age
            max_income = max(max_income, salary)
            min_income = min(min_income, salary)
            count += 1

    # Print the last line
    if last_age:
        print(f'COUNT: {count} | AGE: {last_age} | MIN: {min_income} | MAX: {max_income}')


if __name__ == "__main__":
    main()
