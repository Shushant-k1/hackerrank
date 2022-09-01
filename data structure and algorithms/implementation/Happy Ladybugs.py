#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#
from collections import Counter
def happyLadybugs(b):
    # Write your code here
    No="NO"
    Yes="YES"
    b=list(b)
    a=Counter(b)
    for i in a:
        if i!="_":
            if a[i]==1 :
                return No
    for i in a:
        if i=="_":
            return Yes
    b=list(b)
    c=1
    for i in range(len(b)-1):
        if b[i]==b[i+1]:
            c=c+1
        else:
            if c>=2:
                c=1
            else:
                return No
    return Yes
for i in range(int(input())):
    z=input()
    b=input()
    print(happyLadybugs(b))
