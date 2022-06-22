import re

n = int(input())
line = []
for _ in range(n):
    line.append(input())

q = int(input())
querie = []
for _ in range(q):
    querie.append(input())

for quer in querie:
    pattern = r'\w+'+quer+'\w+'
    # print(pattern)
    count = 0
    for lin in line:
        count += len(re.findall(pattern,lin))
    print(count)
