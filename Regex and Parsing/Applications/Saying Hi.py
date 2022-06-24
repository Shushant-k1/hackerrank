# Enter your code here. Read input from STDIN. Print output to STDOUT

#r"[hH][Ii]\s[^dD]"
import re

pattern=r"^(h|H)(I|i)\s[^dD]"
for i in range(int(input())):
    s=input()
    if re.match(pattern,s):
        print(s)
    
