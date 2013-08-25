# -*- coding: utf-8 -*-
# ProjectEuler/src/python/util.py

import math
import operator


def cached(f):
    f._cache = {}
    def wrapper(n):
        if n not in f._cache:
            f._cache[n] = f(n)
        return f._cache[n]
    return wrapper


@cached
def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def product(iterable):
    return reduce(operator.mul, iterable)


def iter_primes(max_n):
    return (n for n in xrange(1, max_n+1) if is_prime(n))


def divisors(n):
    results = []
    for i in range(1, n):
        if n % i == 0:
            results.append(i)
    return results


def proper_divisors(n):
    results = []
    for i in range(1, n/2 + 1):
        if n % i == 0:
            results.append(i)
    return results


def sum_of_digits(n):
    return sum(int(d) for d in str(n) if d in "0123456789")
