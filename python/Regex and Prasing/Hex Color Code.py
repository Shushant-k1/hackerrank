# take care of {6} and {3} 6 must be at first in or otherwise it will not match
#first(#) is neglected by taking string as input()[:-1]

import re
pattern=r"#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}"
for i in range(int(input())):
    for j in re.findall(pattern,input()[1:]):
        print(j)
