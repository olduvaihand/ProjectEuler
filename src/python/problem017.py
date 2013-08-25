# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem017.py
#
# Number letter counts
# ====================
# Published on Friday, 17th May 2002, 06:00 pm
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the
# numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.

#import projecteuler as pe

NAMES = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
  100: "hundred",
  1000: "thousand",
}


def int_to_string(i):
    parts = []
    if i >= 1000:
        parts.append(NAMES[i/1000])
        parts.append(NAMES[1000])
        i -= 1000
    if i >= 100:
        hundreds = i/100
        d = hundreds * 100
        parts.append(NAMES[hundreds])
        parts.append(NAMES[100])
        i -= d
        if i:
            parts.append("and")
    if i >= 20:
        tens = i / 10 * 10
        ones = i % 10
        parts.append(NAMES[tens])
        if ones:
            parts.append(NAMES[ones])
    elif i:
        parts.append(NAMES[i])
    return " ".join(parts)


def count_letters(n):
    total = 0
    for i in range(1, n+1):
        s = int_to_string(i)
        total += sum(len(x) for x in s.split())
    return total


def main():
    total = count_letters(1000)
    print "Total letters:", total


if __name__ == "__main__":
    main()
