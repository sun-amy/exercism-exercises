"""
Reverse a string.
"""

def reverse(text):
    reversed = ""
    for i in range(0, len(text)):
        reversed += text[i * -1 - 1]
    return reversed
