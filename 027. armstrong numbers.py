"""
Determine if a number is an Armstrong number.

Note: An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
"""

def is_armstrong_number(number):
    total = 0
    number_as_string = str(number)
    for digit in number_as_string:
        total += int(digit) ** len(number_as_string)
    return total == number
