# Python program for the above approach
# v = note jo banana hai
# n = no of elements in arraya
# a =  array of coins
def coinchange(a, v, n, dp):
    if (v == 0):
        return 1
    if (n == 0):
        return 0
    if (dp[v][n] != -1):
        return dp[v][n]
    if (a[n - 1] <= v):
        # Either Pick this coin or not
        dp[v][n] = coinchange(a, v - a[n - 1], n, dp) + \
            coinchange(a, v, n - 1, dp)
        return dp[v][n]
    else: # We have no option but to leave this coin
        dp[v][n] = coinchange(a, v, n - 1, dp)
        return dp[v][n]


if __name__ == '__main__':
    v , n = map(int,input().split())
    a = list(map(int, input().split()))
    tc = 1
    while (tc != 0):
        dp = [[-1 for i in range(n+1)] for j in range(v+1)]
        res = coinchange(a, v, n, dp)
        print(res)
        tc -= 1
