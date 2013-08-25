# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem149.py
#
# Searching for a maximum-sum subsequence.
# ========================================
# Published on Friday, 13th April 2007, 10:00 pm
#
# Looking at the table below, it is easy to verify that the maximum possible
# sum of adjacent numbers in any direction (horizontal, vertical, diagonal or
# anti-diagonal) is 16 (= 8 + 7 + 1).  2532 9651 3273 184  8  Now, let us
# repeat the search, but on a much larger scale: First, generate four million
# pseudo-random numbers using a specific form of what is known as a "Lagged
# Fibonacci Generator": For 1  k  55, sk = [100003  200003k + 300007k3] (modulo
# 1000000)  500000.  For 56  k  4000000, sk = [sk24 + sk55 + 1000000] (modulo
# 1000000)  500000. Thus, s10 = 393027 and s100 = 86613. The terms of s are
# then arranged in a 20002000 table, using the first 2000 numbers to fill the
# first row (sequentially), the next 2000 numbers to fill the second row, and
# so on. Finally, find the greatest sum of (any number of) adjacent entries in
# any direction (horizontal, vertical, diagonal or anti-diagonal).

import projecteuler as pe

def main():
    pass

if __name__ == "__main__":
    main()
