# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem036.py
#
# Double-base palindromes
# =======================
# Published on Friday, 31st January 2003, 06:00 pm
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number, in either base,
# may not include leading zeros.)

def double_base_palindromes(max_n):
    palindromes = []
    for i in range(max_n+1):
        s = str(i)
        b = bin(i)[2:]
        if s == "".join(reversed(s)) and b == "".join(reversed(b)):
            palindromes.append(i)
    return palindromes


def main():
    palindromes = double_base_palindromes(1000000)
    print "The sum of all double base palindromes under 1000000 is:",
    print sum(palindromes)


if __name__ == "__main__":
    main()
