"""
Given a year, report if it is a leap year.
"""

def leap_year(year):
    four = year % 4
    hundred = year % 100
    four_hundred = year % 400
    if four == 0:
        if hundred != 0:
            return True
        else:
            if four_hundred == 0:
                return True
    return False
