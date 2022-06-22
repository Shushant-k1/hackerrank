# Enter your code here. Read input from STDIN. Print output to STDOUT
#  ^[A-Z]{5}[\d]{4}[A-Z]$ or (\d)
import re
pattern=r"^[A-Z]{5}\d{4}[A-Z]$"
for i in range(int(input())):
    a=re.match(pattern,input())
    if a:
        print("YES")
    else:
        print("NO")
