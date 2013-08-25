﻿# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem028.py
#
# Number spiral diagonals
# =======================
# Published on Friday, 11th October 2002, 06:00 pm
#
# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows: 21 22 23 24 25  20  7  8  9 10  19  6  1
# 2 11  18  5  4  3 12 17 16 15 14 13 It can be verified that the sum of the
# numbers on the diagonals is 101. What is the sum of the numbers on the
# diagonals in a 1001 by 1001 spiral formed in the same way?

import util


@util.cached
def lower_right(n):
    if n == 1:
        return 0
    return upper_right(n-2) + n-1


@util.cached
def lower_left(n):
    if n == 1:
        return 0
    return lower_right(n) + n-1


@util.cached
def upper_left(n):
    if n == 1:
        return 0
    return lower_left(n) + n-1


@util.cached
def upper_right(n):
    if n == 1:
        return 1
    return n*n


def sum_of_diagonals(max_size):
    total = 0
    for i in xrange(1, max_size+1, 2):
        total += upper_right(i)
        total += lower_right(i)
        total += lower_left(i)
        total += upper_left(i)
    return total


def main():
    total = sum_of_diagonals(1001)
    print "The sum of the diagonals of a 1001x1001 grid is: %d" % (total,) 


if __name__ == "__main__":
    main()