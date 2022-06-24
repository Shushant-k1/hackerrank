# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern=r"^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$"
for i in range(int(input())):
    a=input()
    if re.match(pattern,a):
        print("VALID")
    else:
        print("INVALID")
