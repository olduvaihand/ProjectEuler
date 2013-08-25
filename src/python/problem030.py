# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem030.py
#
# Digit fifth powers
# ==================
# Published on Friday, 8th November 2002, 06:00 pm
#
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits: 1634 = 14 + 64 + 34 + 44 8208 = 84 + 24 + 04 +
# 84 9474 = 94 + 44 + 74 + 44 As 1 = 14 is not a sum it is not included. The
# sum of these numbers is 1634 + 8208 + 9474 = 19316. Find the sum of all the
# numbers that can be written as the sum of fifth powers of their digits.


def digit_fifth_powers():
    res = []
    powers = {str(x): x**5 for x in range(10)}
    for i in xrange(10, 5 * 9**5):
      digits = str(i)
      sum_of_digits = sum(powers[d] for d in digits)
      if sum_of_digits == i:
        res.append(i)
    return res


def main():
    dfp = digit_fifth_powers()
    print "The sum of all digit fifth powers is:", sum(dfp)


if __name__ == "__main__":
    main()
