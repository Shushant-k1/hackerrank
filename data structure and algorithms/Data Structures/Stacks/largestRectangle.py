def largestRectangle(h):
    ans = 0
    for  i in range(len(h)) :
        j = i
        cnt = 0
        while j < len(h) and h[i] <= h[j] :
            j += 1
            cnt += 1
        j = i  - 1
        while j >= 0 and h[i] <= h[j] :
            j -= 1
            cnt += 1
        ans = max(ans , cnt * h[i])
    return ans
