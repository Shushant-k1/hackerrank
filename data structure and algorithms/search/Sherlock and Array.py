#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    a = []
    s = 0
    for i in arr:
        s = s + i
        a.append(s)
    print(a)
    if a[0] == a[-1] or (a[0]==0 and a[-1] == s) :
        return "YES"
    else:
        for i in range(1,len(arr)-1) :
            x = s - a[i]
            y = a[i-1]
            print(x , y)
            if x == y :
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
