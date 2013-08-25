# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem020.py
#
# Factorial digit sum
# ===================
# Published on Friday, 21st June 2002, 06:00 pm
#
# n! means n  (n  1)  ...  3  2  1 For example, 10! = 10  9  ...  3  2  1 =
# 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0
# + 0 = 27. Find the sum of the digits in the number 100!

import math

import util


def main():
    sum_of_digits = util.sum_of_digits(math.factorial(100))
    print "The sum of the digits in 100! is %d." % (sum_of_digits,)

if __name__ == "__main__":
    main()
