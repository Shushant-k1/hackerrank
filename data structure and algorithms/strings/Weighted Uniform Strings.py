s = input()
scores = set()
ctr=1
for i in range(len(s)):
    ctr = ctr+1 if i+1 != len(s) and s[i+1] == s[i] else 1
    scores.add((ord(s[i])-96)*ctr)
for n in range(int(input())):
    print("Yes" if int(input()) in scores else "No")
