'''
This is a python program to calculate the day of the week using Zeller's Congruence.
q = date
m = month
y = year
'''

import math

class DateCalculator:
    def __init__(self, q, m, y):
        self.y = y
        self.m = m
        self.q = q

        # Adjust the months January and February
        if m == 1 or m == 2:
            self.m += 12
            self.y -= 1


    # Function to compute day of the week
    def computeDay(self):
        K = self.y % 100
        J = self.y // 100

        h = (self.q + math.floor((13 * (self.m + 1)) / 5) + K + math.floor(K / 4) + math.floor(J / 4) + (5*J)) % 7

        days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print("Day of the week is " + days_of_the_week[h-1])



dateCalculator = DateCalculator(1, 5, 2025)
dateCalculator.computeDay()
