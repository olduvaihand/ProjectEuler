# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem040.py
#
# Champernowne's constant
# =======================
# Published on Friday, 28th March 2003, 06:00 pm
#
# An irrational decimal fraction is created by concatenating the positive
# integers: 0.123456789101112131415161718192021... It can be seen that the 12th
# digit of the fractional part is 1. If dn represents the nth digit of the
# fractional part, find the value of the following expression. d1  d10  d100
# d1000  d10000  d100000  d1000000

import util

def main():
    decimal = "".join(str(i) for i in xrange(1,1000000))[:1000000]
    digits = (int(decimal[i-1]) for i in (10**j for j in xrange(7)))
    print "The product of d1 * d10 * d100 * d1000 * d10000 * d100000",
    print "* d1000000 is:", util.product(digits)

if __name__ == "__main__":
    main()
