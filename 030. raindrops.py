"""
Convert a number to a string, the content of which depends on the number's factors.
"""

def convert(number):
    rain_sounds = ""
    if number % 3 == 0:
        rain_sounds += "Pling"
    if number % 5 == 0:
        rain_sounds += "Plang"
    if number % 7 == 0:
        rain_sounds += "Plong"
    if rain_sounds == "":
        return str(number)
    return rain_sounds
