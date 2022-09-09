#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.
# xor of 8  elements is equal to 2
# so we have to calculate for the xor which are not multiples of 8 
def sequence(N):
    x = N % 8
    if x == 0 or x == 1:
        return N
    if x == 2 or x == 3:
        return 2
    if x == 4 or x == 5:
        return N+2
    if x == 6 or x == 7:
        return 0

def xorSequence(l, r):
    return sequence(r) ^ sequence(l-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
