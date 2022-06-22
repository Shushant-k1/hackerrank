# Enter your code here. Read input from STDIN. Print output to STDOU
import re
for i in range(int(input())):
    pattern=r'^[_.]\d+[a-zA-Z]*[_]?$'
    m=re.search(pattern,input())
    if m:
        print("VALID")
    else:
        print("INVALID")
