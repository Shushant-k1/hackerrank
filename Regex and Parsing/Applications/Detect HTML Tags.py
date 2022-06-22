#    \s for take care of space
#take care of opening tag not look into the closing tag


Regex = r'<\s*(\w+)'
import re

list = set()

for _ in range(int(input())):
    _t = input()
    found = re.findall(Regex, _t)
    for tag in found:
        if tag not in list:
            list.add(tag)

print(';'.join(sorted(list)))
