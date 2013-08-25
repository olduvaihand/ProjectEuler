# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem041.py
#
# Pandigital prime
# ================
# Published on Friday, 11th April 2003, 06:00 pm
#
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime. What is the largest n-digit pandigital prime that exists?

import util


def pandigital_prime(n_digits):
    if n_digits % 2 == 0:
        start = int(str(n_digits) * n_digits) + 1
    else:
        start = int(str(n_digits) * n_digits)
    end = 10**(n_digits - 1)
    digits = set("".join(str(d) for d in xrange(1, n_digits + 1)))
    for i in xrange(start, end, -2):
        if set(str(i)) == digits:
            if util.is_prime(i):
                return i


def main():
    pd = None
    for i in xrange(7, 0, -1):
        pd = pandigital_prime(i)
        if pd:
            break
    print "The largest pandigital prime is:", pd

if __name__ == "__main__":
    main()
