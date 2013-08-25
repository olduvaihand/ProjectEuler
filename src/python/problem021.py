# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem021.py
#
# Amicable numbers
# ================
# Published on Friday, 5th July 2002, 06:00 pm
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).  If d(a) = b and d(b) = a, where a  b, then a
# and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220. Evaluate the sum of all the amicable numbers
# under 10000.

import math

import util


def sum_of_amicable_numbers(max_n):
    n_to_sum = {}
    for n in range(1, max_n + 1):
        sum_of_divisors = sum(util.divisors(n))
        n_to_sum[n] = sum_of_divisors
    amicable = (n for n, sod in n_to_sum.iteritems()
                if n_to_sum.get(sod, 0) == n and n != sod)
    return sum(amicable)


def main():
    total = sum_of_amicable_numbers(10000)
    print "The sum of all amicable numbers under 10000 is %d." % (total,)

if __name__ == "__main__":
    main()
