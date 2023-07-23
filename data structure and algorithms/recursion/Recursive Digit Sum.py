def su(digit) :
    if digit < 10 :
        return digit
    return digit % 10 + su(digit//10)

def co( di):
    if di < 10 :
        return di
    return co(su(di))

def superDigit(n, k):
    # Write your code here
    x = 0
    for i in range(len(n)) :
        x = x + k * int(n[i])
    return co(x)
