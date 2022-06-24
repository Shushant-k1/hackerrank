# Enter your code here. Read input from STDIN. Print output to S
import re

pattern1=r"^hackerrank"
pattern2=r"hackerrank$"
#pattern0=r"^hackerrank$"

for i in range(int(input())):
    a=input()
    b=re.findall(pattern1,a)
    c=re.findall(pattern2,a)
    #d=re.search(pattern0,a)
    if (b or c):
        if b and c:
            print("0")
        elif b:
            print("1")
        elif c:
            print("2")
    else:
        print("-1")
    
        
    
