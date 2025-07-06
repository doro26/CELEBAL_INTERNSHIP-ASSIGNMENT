# This script reads a string and groups consecutive identical characters using itertools.groupby.
# For each group, it prints a tuple showing the count of consecutive characters and the character itself.
# Useful for learning how to use the groupby function to compress or summarize repeated data sequences.
# Helps practice iteration, grouping, and string manipulation in Python.

from itertools import groupby

string=input()

for key,group in groupby(string):
    count = len(list(group))
    print(f"({count}, { key})",end=' ')
