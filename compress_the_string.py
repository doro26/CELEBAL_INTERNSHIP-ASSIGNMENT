from itertools import groupby

string=input()

for key,group in groupby(string):
    count = len(list(group))
    print(f"({count}, { key})",end=' ')