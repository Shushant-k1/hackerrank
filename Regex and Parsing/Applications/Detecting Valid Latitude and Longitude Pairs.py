# Enter your code here. Read input from STDIN. Print output to STDOUT 
# take care of capuring group using proper brackets
'''
import re
for i in range(int(input())):
    s = input()
    if re.search(r'^\([+-]?(90(\.0+)?|(([1-8]?\d)(\.\d+)?)), [+-]?(180(\.0+)?|(1[0-7]|[1-9])\d(\.\d+)?)\)$', s):
        print('Valid')
    else:
        print('Invalid')
'''
import re

n = int(input())

Reg = r"\([+\-]?(90(\.0+)?|[1-8]\d(\.\d+)?|\d(\.\d+)?), [+\-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|\d{2}(\.\d+)?|\d(\.\d+)?)\)"

for _ in range (n):
    p = input()
    print("Valid" if re.match(Reg,p) is not None else "Invalid")
