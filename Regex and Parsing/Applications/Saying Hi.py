# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern=r"^(h|H)(I|i)\s[^d]"
for i in range(int(input())):
    s=input()
    if re.match(pattern,s):
        print(s)
    
