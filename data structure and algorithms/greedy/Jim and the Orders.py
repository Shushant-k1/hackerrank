#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    x = []
    z = []
    m = 0
    for i in range(len(orders)):
        x.append([sum(orders[i]),i])
    a = sorted(x, key=lambda x: x[1])
    a = sorted(a, key=lambda x: x[0])
    for i in range(len(a)):
        m = a[i][1]
        z.append(m+1)
    return z
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
