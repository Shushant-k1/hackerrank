# Enter your code here. Read input from STDIN. Print output to STDOUT
# serch will match from the any index
# but match will match from starting


import re
pattern=r"(hackerrank)"
count=0
for i in range(int(input())):
    if re.search(pattern,input(),re.IGNORECASE):
        count=count+1
print(count)
    
 
