# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem022.py
#
# Names scores
# ============
# Published on Friday, 19th July 2002, 06:00 pm
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score. For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
# COLIN would obtain a score of 938  53 = 49714. What is the total of all the
# name scores in the file?

import csv
import os
import string


LETTER_VALUES = {
    l: string.ascii_uppercase.index(l) + 1
    for l in string.ascii_uppercase
}


def calculate_name_score(position, name):
    return position * sum(LETTER_VALUES[l] for l in name)


def sum_of_name_scores(names):
    total = 0
    for i, name in enumerate(names, 1):
        total += calculate_name_score(i, name)
    return total


def main():
    data_path = os.path.join(os.path.dirname(__file__), "data", "names.txt")
    with open(data_path) as f:
        reader = csv.reader(f)
        names = reader.next()
    names.sort()
    total = sum_of_name_scores(names)
    print "The total of all name scores is %d." % (total,)


if __name__ == "__main__":
    main()
