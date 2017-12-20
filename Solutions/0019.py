"""
# PROBLEM 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# I guess `import date` is cheating, right?
# (obligatory xkcd: https://xkcd.com/353/)

months = ["JA", "FE", "MR", "AP", "MA", "JU", "JL", "AU", "SE", "OC", "NO", "DE"]

days_in_month = {
    "JA": 31,
    "MR": 31,
    "AP": 30,
    "MA": 31,
    "JU": 30,
    "JL": 31,
    "AU": 31,
    "SE": 30,
    "OC": 31,
    "NO": 30,
    "DE": 31
}


def ym(year, month):
    if not month == 'FE':
        return days_in_month[month]
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    else:
        return 28


count = 0
cur_year = 1900
cur_day = 1
cur_wd = 0
cur_month = 0
days_this_month = ym(cur_year, months[cur_month])

while cur_year < 2001:
    if cur_wd == 6 and cur_day == 1 and cur_year > 1900:
        count += 1

    cur_wd = (cur_wd + 1) % 7

    if cur_day == days_this_month:
        if cur_month == 11:
            cur_month = 0
            cur_year += 1
        else:
            cur_month += 1
        days_this_month = ym(cur_year, months[cur_month])
        cur_day = 1
    else:
        cur_day += 1

print(count)
