def print_formatted(number):
    # your code goes here
    
    length=len(bin(number))-2
    
    for i in range(1,number+1):
        decimal=str(i)
        octal=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        binary=bin(i)[2:]
        
        print(decimal.rjust(length),octal.rjust(length),hexa.rjust(length),binary.rjust(length))

