# -*- coding: utf-8 -*-
# ProjectEuler/src/python/problem019.py
#
# Counting Sundays
# ================
# Published on Friday, 14th June 2002, 06:00 pm
#
# You are given the following information, but you may prefer to do some
# research for yourself.  1 Jan 1900 was a Monday. Thirty days has September,
# April, June and November. All the rest have thirty-one, Saving February
# alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.  How many Sundays fell on the first of the
# month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

MON, TUE, WED, THU, FRI, SAT, SUN = range(1,8)
MONTHS = JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = range(12)
SHORT_MONTHS = set([APR, JUN, SEP, NOV])


def is_a_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def month_length(year, month):
    if month == FEB:
        if is_a_leap_year(year):
            return 29
        else:
            return 28
    return 30 if month in SHORT_MONTHS else 31


def is_sunday(days):
    return days % SUN == 0


def count_sundays_since_1901(end_year):
    count = 0
    days = 1 + 365
    for year in xrange(1901, end_year+1):
        for month in MONTHS:
            if is_sunday(days):
                count += 1
            days += month_length(year, month)
    return count


def main():
    count = count_sundays_since_1901(2000)
    print count, "Sundays fell on the first of the month in the 20th century."


if __name__ == "__main__":
    main()
