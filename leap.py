"""
    Leap year:
        1. Evenly divided by 4, it's a leap year, unless:
        2. Evenly divided by 100, it is NOT a leap year, unless:
        3. Evenly divisible by 400, it's a leap year
"""

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True

    return leap


year = int(input())
print(is_leap(year))