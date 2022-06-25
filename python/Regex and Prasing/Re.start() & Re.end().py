import re
s,k=input(),input()



if(bool(re.findall(k,s))):
    
    for i in range(len(s)):
        if(bool(re.match(k,s[i:]))):
            print((i,i+len(k)-1))
else:
     print((-1,-1))   
