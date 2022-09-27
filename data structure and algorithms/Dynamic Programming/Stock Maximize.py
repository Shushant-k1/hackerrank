#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    a = max(prices)
    maxs = 0
    x = []
    for i in range(len(prices)-1,-1,-1):
        maxs = max(maxs,prices[i])
        x.append(maxs)
    x = x[:]
    x = x[::-1]
    ans = 0
    for i in range(len(prices)):
        ans = ans + x[i] - prices[i]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
