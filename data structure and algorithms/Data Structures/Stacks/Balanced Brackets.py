
for k in range(int(input())):
    a=[]
    b=list(input())
    c=len(b)
    bool=True
    for i in range(c):
        if (b[i]=="(") or (b[i]=="{") or (b[i]=="["):
            a.append(b[i])
        else:
            if b[i]==")":
                if len(a)==0:
                    bool=False
                    break 
                elif a[-1]=="(":
                    bool=True
                    a.pop()
                else:
                    bool=False
                    break
            elif b[i]=="}":
                if len(a)==0:
                    bool=False
                    break
                elif a[-1]=="{":
                    bool=True
                    a.pop()
                else:
                    bool=False
                    break
            elif b[i]=="]":
                if len(a)==0:
                    bool=False
                    break
                elif a[-1]=="[":
                    bool=True
                    a.pop()
                else:
                    bool=False
                    break  
    if bool==True and len(a)==0:
        print("YES")
    else:
        print("NO")
