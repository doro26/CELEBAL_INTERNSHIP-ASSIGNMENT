# Enter your code here. Read input from STDIN. Print output to STDOUT
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
        
