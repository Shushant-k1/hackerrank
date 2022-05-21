#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    b=a[0]
    c=0
    mx=0
    for i in range(len(a)):
        if a[i]==b or a[i]==b+1:
            c=c+1
            mx=max(c,mx)
        else:
            mx=max(c,mx)
            b=a[i]
            c=1
    return mx
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
