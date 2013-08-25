# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem023.py
#
# Non-abundant sums
# =================
# Published on Friday, 2nd August 2002, 06:00 pm
#
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.  As 12 is the smallest
# abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis,
# it can be shown that all integers greater than 28123 can be written as the
# sum of two abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest number that
# cannot be expressed as the sum of two abundant numbers is less than this
# limit. Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

import util


MINIMUM_ABUNDANT_NUMBER = 12


def is_abundant(n):
    divisors = util.proper_divisors(n)
    return sum(divisors) > n


def calculate_abundant_numbers(max_n):
    return [n for n in range(1, max_n) if is_abundant(n)]


def non_abundant_sums(max_n):
    sums = []
    abundant_numbers = calculate_abundant_numbers(max_n)
    abundant_set = set(abundant_numbers)
    for i in range(1, max_n+1):
        for a in abundant_numbers:
            difference = i - a
            if difference < MINIMUM_ABUNDANT_NUMBER:
                sums.append(i)
                break
            if difference in abundant_set:
                break
        else:
            sums.append(i)
    return sum(sums)


def main():
    total = non_abundant_sums(28123)
    print "The sum of all positive integers which cannot be written as the ",
    print "sum of 2 abundant numbers is %d." % (total,)


if __name__ == "__main__":
    main()
