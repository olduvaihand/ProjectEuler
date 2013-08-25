# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem033.py
#
# Digit canceling fractions
# =========================
# Published on Friday, 20th December 2002, 06:00 pm
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by cancelling the 9s. We shall consider fractions
# like, 30/50 = 3/5, to be trivial examples. There are exactly four non-trivial
# examples of this type of fraction, less than one in value, and containing two
# digits in the numerator and denominator. If the product of these four
# fractions is given in its lowest common terms, find the value of the
# denominator.

'''
def get_numbers(i):
  ones = i % 10
  tens = i - ones
  res = set([(ones, 10*x) + ones for x in range(1,10)] + [(tens / 10, tens + x) for x in range(10)])
  return res

for i in range(10,100):
  ns = get_numbers(i)
  for x, n in ns:
    if i < n:
      num = i
      den = n
    else:
      num = n
      den = i
    f = num/den
'''


def main():
    pass

if __name__ == "__main__":
    main()
