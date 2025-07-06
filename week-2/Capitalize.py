def solve(s):
    name=''
    cap_name = True
    for i in s:
        if i == ' ':
            name += i
            cap_name = True
        elif cap_name:
            name += i.upper()
            cap_name = False
        else:
            name += i
    return name     