# This script calculates the probability that a randomly chosen combination of size K
# from a list of elements contains the character 'a'.
# It uses itertools.combinations to generate all possible combinations,
# counts those including 'a', and computes the ratio of such combinations to total combinations.
# A practical example to learn about combinatorics, use of itertools, and probability calculation in Python.


import itertools
N=int(input())
L=input().split()
K=int(input())
count =0
tuples=list(itertools.combinations(L,K))
for i in tuples:
    if 'a' in i:
        count += 1;
        
length = len(tuples)
probability=count/length
print(round(probability,4))        
        
