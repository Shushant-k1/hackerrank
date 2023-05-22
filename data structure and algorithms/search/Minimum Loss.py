def minimumLoss(price):
    # Write your code here
    d = {} 
    for i in range(len(price)) :
        d[price[i]] =  i
    price.sort()
    ans = 100000000000000000000000000
    # do in copy u will get logic
    # the logic is minimum diffrece is when we get we substract from the ajacent number and therir is index is after that
    # index we get from the hash array
    for i in range(1 ,len(price)) :
        if d[price[i - 1]] > d[price[i]] :
            ans = min(ans , price[i] - price[i - 1])
    return ans
