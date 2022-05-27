# idea for solution
#make a cobinations of all numbers 
# then take a or operations 
#take care of given daat in string 
#use builtin features itertools combinations



#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    maxTeam = 0
    maxKnownTopic = 0
    comb = combinations(topic,2)
    #make combinations
    #print(list(comb))
    for i in comb:
        n = bin(((int(i[0],2) | int(i[1],2)))).count('1')
        # or operator
        if maxKnownTopic < n:
            maxKnownTopic = n
            maxTeam = 1
        elif n == maxKnownTopic:
            maxTeam +=1
    return  maxKnownTopic , maxTeam
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
