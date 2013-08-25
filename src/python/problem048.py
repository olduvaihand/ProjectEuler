# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem048.py
#
# Self powers
# ===========
# Published on Friday, 18th July 2003, 06:00 pm
#
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317. Find the last ten digits
# of the series, 11 + 22 + 33 + ... + 10001000.

def main():
    answer = str(sum(i**i for i in xrange(1, 1001)))[-10:]
    print "The last 10 digits in the sum of the series is %s." % (answer,)

if __name__ == "__main__":
    main()
