def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        left = alphabet[size-1:i:-1]
        mid = alphabet[i:size]
        s = '-'.join(left + mid)
        lines.append(s.center(4*size - 3, '-'))
    full = lines[::-1] + lines[1:]
    for line in full:
        print(line)

