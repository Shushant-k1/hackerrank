# can be solved with dp
# concept of 0 1 knapsack

# this can be solved by using a pattern
# 1,7,8,14,15 second else 1

# This code is submitted by "Shushant kumar"

t = int(input())
for _ in range(t):
    s = int(input())
    if s % 7 < 2:
        print ('Second')
    else:
        print ('First')
    
