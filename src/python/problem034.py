# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem034.py
#
# Digit factorials
# ================
# Published on Friday, 3rd January 2003, 06:00 pm
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. Find the sum
# of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math


FACTORIALS = {str(i): math.factorial(i) for i in range(10)}


def digit_factorials():
    res = []
    for i in xrange(3, FACTORIALS["9"]):
        if i == sum(FACTORIALS[d] for d in str(i)):
            res.append(i)
    return res


def main():
    df = digit_factorials()
    print "The sum of all digit factorials is:", sum(df)


if __name__ == "__main__":
    main()
