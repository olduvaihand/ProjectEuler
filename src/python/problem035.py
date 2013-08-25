# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem035.py
#
# Circular primes
# ===============
# Published on Friday, 17th January 2003, 06:00 pm
#
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime. There are thirteen such
# primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How
# many circular primes are there below one million?

import itertools
import re

import util

EVENS = re.compile(r"[02468]")


def circular_primes(max_n):
    res = []
    for i in itertools.chain((2,), xrange(3, max_n + 1, 2)):
        s = str(i)
        l = len(s)
        if l > 1 and any([EVENS.search(s), "5" in s]):
            continue
        permutations = [int("".join(p)) for p in itertools.permutations(s, l)]
        for p in permutations:
            if not util.is_prime(p):
                break
        else:
            res.extend(permutations)
    return res


def main():
    cp = circular_primes(1000000)
    print "The number of circular primes < 1000000 is:", len(cp)


if __name__ == "__main__":
    main()
