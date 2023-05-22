#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
# top down approach
# def lcs(s1 , s2 , x , y , dp ) :
#     if x == 0 or y == 0 :
#         return 0
#     if dp[x][y] != -1 :
#         return dp[x][y]
#     if s1[x-1] == s2[y-1] :
#         dp[x][y] =  1 + lcs(s1 , s2 ,x - 1 , y - 1 , dp)
#         return dp[x][y]
#     else :
#         dp[x][y] =  max(lcs(s1 , s2 , x , y - 1 , dp) , lcs(s1 , s2 , x-1, y , dp)) 
#         return dp[x][y]

# def commonChild(s1, s2):
#     # Write your code here
#     n = len(s1)
#     m = len(s2)
#     dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]
#     return lcs(s1 , s2 , len(s1) , len(s2) ,dp)
# bottom up approach
def commonChild(X , Y, m, n):    

    # Declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2 , len(s1) , len(s2))

    fptr.write(str(result) + '\n')

    fptr.close()
