import re
pattern=r"^[789]\d{9}$"
for i in range(int(input())):
    if re.match(pattern,input()):
        print("YES")
    else:
        print("NO")
