# This code prints numbers from 1 to 'number' in different formats:
# decimal, octal, hexadecimal (uppercase), and binary.
# It makes sure all the outputs line up nicely by adding spaces before the numbers.
# The width for spacing is based on the length of the binary form of the largest number.
# Functions like bin(), oct(), and hex() add prefixes like '0b', '0o', and '0x',
# so we remove those with [2:] to get just the number part.
# rjust() adds spaces on the left so everything aligns evenly.

def print_formatted(number):
    # your code goes here
    
    length=len(bin(number))-2
    
    for i in range(1,number+1):
        decimal=str(i)
        octal=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        binary=bin(i)[2:]
        
        print(decimal.rjust(length),octal.rjust(length),hexa.rjust(length),binary.rjust(length))

