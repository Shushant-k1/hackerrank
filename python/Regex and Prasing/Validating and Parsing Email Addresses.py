# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>'
for i in range(int(input())):
    s,y=input().split()
    if re.match(pattern,y):
        print(s,y)
