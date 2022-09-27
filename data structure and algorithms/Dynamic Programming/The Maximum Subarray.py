#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    cur = 0
    maxs = - (10**4)
    sub = max(arr)
    if sub < 0 :
        pass
    else :
        sub = 0
        for i in arr :
            if i >= 0:
              sub = sub + i  
    for i in arr:
        cur = cur + i
        maxs = max(maxs , cur)
        if cur < 0:
            cur = 0
       
    return maxs , sub
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
