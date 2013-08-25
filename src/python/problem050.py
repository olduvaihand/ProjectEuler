# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem050.py
#
# Consecutive prime sum
# =====================
# Published on Friday, 15th August 2003, 06:00 pm
#
# The prime 41, can be written as the sum of six consecutive primes: 41 = 2 + 3
# + 5 + 7 + 11 + 13 This is the longest sum of consecutive primes that adds to
# a prime below one-hundred. The longest sum of consecutive primes below one-
# thousand that adds to a prime, contains 21 terms, and is equal to 953. Which
# prime, below one-million, can be written as the sum of the most consecutive
# primes?

import util


def longest_consecutive_prime_sum(max_n):
    primes = list(util.iter_primes(max_n))
    primes_set = set(util.iter_primes(max_n))
    running_sums = [2]
    for p in primes[1:]:
        running_sums.append(running_sums[-1] + p)
    max_start, max_end = 0, len(running_sums) - 1 
    max_length = 0
    for end in xrange(len(running_sums) - 1, -1, -1):
        for start in xrange(0, end):
            diff = running_sums[end] - running_sums[start]
            length = end - start
            if length > max_length and diff in primes_set:
                max_length = length
                max_start, max_end = start, end
                break
            if length < max_length:
                break
    return running_sums[max_end] - running_sums[max_start], max_length


def main():
    lcps, length = longest_consecutive_prime_sum(1000000)
    print "The longest consecutive prime sum under 1000000 is",
    print "%d, the sum of %d consecutive prime numbers." % (lcps, length)


if __name__ == "__main__":
    main()
