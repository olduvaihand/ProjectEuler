# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem032.py
#
# Pandigital products
# ===================
# Published on Friday, 6th December 2002, 06:00 pm
#
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital. The product 7254 is unusual, as the identity, 39  186 =
# 7254, containing multiplicand, multiplier, and product is 1 through 9
# pandigital. Find the sum of all products whose
# multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital. HINT: Some products can be obtained in more than one way so be
# sure to only include it once in your sum.


DIGITS = {i: set("".join(str(j) for j in xrange(1,i+1))) for i in xrange(10)}


def pandigital_products(max_n):
    res = set()
    for i in range(1, max_n):
        j_limit = 10**(6-len(str(i))) - 1
        for j in range(1, j_limit):
            p = i * j
            s = "%d%d%d" % (i, j, p)
            if len(s) != 9:
                continue
            if DIGITS[len(s)] == set(s):
                res.add(p)
    return res


def main():
    pp = pandigital_products(10000)
    print "The sum of all pandigital products is:", sum(pp)


if __name__ == "__main__":
    main()
