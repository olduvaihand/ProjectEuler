# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem016.py
#
# Power digit sum
# ===============
# Published on Friday, 3rd May 2002, 06:00 pm
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. What is the
# sum of the digits of the number 21000?

import util


def main():
    s = util.sum_of_digits(2**1000)
    print "The sum of the digits of the number 2**1000 is: %d" % (s,)

if __name__ == "__main__":
    main()
