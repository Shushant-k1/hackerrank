# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a=input()
_b=input().split()
d=list(combinations(_b,int(input())))
e=0
for i in range(len(d)):
    if "a" in d[i]:
        e=e+1
print(e/len(d))
