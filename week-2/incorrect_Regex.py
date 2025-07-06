import re

for _ in xrange(int(raw_input())):
    try:
        re.compile(raw_input())
        print True
    except:
        print False
