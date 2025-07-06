
# This Python function prints numbers from 1 to a given number in decimal, octal, 
# hexadecimal (uppercase), and binary formats.
# It dynamically adjusts spacing to align the output columns based on the binary 
# representation width of the highest number.
# This helps practice number base conversions, string formatting, and output alignment in Python.
# A useful exercise for understanding different numeral systems and formatting output cleanly.

def print_formatted(number):
    # your code goes here
    
    length=len(bin(number))-2
    
    for i in range(1,number+1):
        decimal=str(i)
        octal=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        binary=bin(i)[2:]
        
        print(decimal.rjust(length),octal.rjust(length),hexa.rjust(length),binary.rjust(length))

