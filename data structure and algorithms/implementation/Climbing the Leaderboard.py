#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked=list(set(ranked))
    ranked.sort()
    ranked=ranked[::-1]
    player=player[::-1]
    a=[]
    i=0
    j=0
    while i<len(player) and j<len(ranked):
        if j>len(ranked):
            a.append(j+1)
            break
        elif player[i]>=ranked[j]:
            a.append(j+1)
            i=i+1
        else:
            j=j+1
    if len(a)==len(player):
        return a[::-1]
    else:
        b=len(player)-len(a)
        for i in range(b):
            a.append(len(ranked)+1)
    return a[::-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
