# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem037.py
#
# Truncatable primes
# ==================
# Published on Friday, 14th February 2003, 06:00 pm
#
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
# left: 3797, 379, 37, and 3. Find the sum of the only eleven primes that are
# both truncatable from left to right and right to left. NOTE: 2, 3, 5, and 7
# are not considered to be truncatable primes.

import util


def truncate(s):
    l = len(s)
    for i in xrange(l):
        yield int(s[i:])
        yield int(s[:l-i])


def is_truncatable_prime(n):
    nb = buffer(str(n))
    return all(map(util.is_prime, truncate(nb)))


def calculate_truncatable_primes():
    truncatable_primes = []
    i = 11
    while len(truncatable_primes) < 11:
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
        i += 2
    return truncatable_primes


def main():
    tp = calculate_truncatable_primes()
    print "The sum of the eleven truncatable primes is:", sum(tp)


if __name__ == "__main__":
  main()
