# This function determines whether a given year is a leap year or not.
# It follows the leap year rules:
# - Year divisible by 4 is a leap year,
# - Except if it is divisible by 100, then it must also be divisible by 400 to be a leap year.
# The function returns True if the year is leap, otherwise False.
# A simple way to practice conditional statements and logical operators in Python.

def is_leap(year):
    leap = False
    
    if(year%4==0 and (year % 100 != 0 or year %400==0)):
        return True
        
    return leap

