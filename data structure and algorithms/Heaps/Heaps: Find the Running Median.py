#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
import heapq as heap
def runningMedian(arr):
    # Print your answer within the function
    # create a max heap and min heap
    max=[]
    min=[]
    for i in range(n):
        if i%2==0:
            if len(max)==0:
                heap.heappush(max,-(arr[i]))
                print(float(-max[0]))
            elif -max[0]<arr[i] and min[0]<arr[i]:
                a=heap.heappop(min)
                heap.heappush(min,(arr[i]))
                heap.heappush(max,-a)
                print(float(-max[0]))
            elif -max[0]<arr[i] and min[0]>arr[i]:
                heap.heappush(max,-(arr[i]))
                print(float(-max[0]))
            else:
                heap.heappush(max,-(arr[i]))
                print(float(-max[0]))
        else:
            if len(min)==0:
                if -max[0]>arr[i]:
                    a=heap.heappop(max)
                    heap.heappush(min,-a)
                    heap.heappush(max,-(arr[i]))
                    print((-max[0]+min[0])/2)
                else:
                    heap.heappush(min,arr[i])
                    print((-max[0]+min[0])/2)
            else:
                if -max[0]<arr[i]:
                    heap.heappush(min,arr[i])
                    print((-max[0]+min[0])/2)
                else:
                    a=heap.heappop(max)
                    heap.heappush(min,-a)
                    heap.heappush(max,-(arr[i]))
                    print((-max[0]+min[0])/2)  
                      
                

if __name__ == '__main__':
    n = int(input().strip())

    a = []

    for _ in range(n):
        a_item = int(input().strip())
        a.append(a_item)

    runningMedian(a)
