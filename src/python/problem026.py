# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem026.py
#
# Reciprocal cycles
# =================
# Published on Friday, 13th September 2002, 06:00 pm
#
# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:    1/2= 0.5   1/3=
# 0.(3)   1/4= 0.25   1/5= 0.2   1/6= 0.1(6)   1/7= 0.(142857)   1/8= 0.125
# 1/9= 0.(1)   1/10= 0.1    Where 0.1(6) means 0.166666..., and has a 1-digit
# recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle. Find
# the value of d < 1000 for which 1/d contains the longest recurring cycle in
# its decimal fraction part.


def divide(numerator, denominator, seen):
    q = numerator / denominator
    r = numerator - (q * denominator)
    if r in seen:
        return len(seen)
    seen.add(r)
    return divide(r * 10, denominator, seen)


def longest_reciprocal_cycle(max_n):
    max_cycle_i = 0
    max_cycle_length = 0
    for i in xrange(max_n, 0, -1):
        if max_cycle_length > i:
            break
        res = divide(1, i, set())
        if res > max_cycle_length:
            max_cycle_length = res
            max_cycle_i = i
    return max_cycle_i

def main():
    d = longest_reciprocal_cycle(1000)
    print "The integer < 1000 with the longest reciprocal cycle is:", d

if __name__ == "__main__":
    main()
