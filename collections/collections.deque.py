from collections import deque
d=deque()
for i in range(int(input())):
    a,*b=input().split()
    getattr(d,a)(*b)
for i in d:
    print(i,end=" ")
    
