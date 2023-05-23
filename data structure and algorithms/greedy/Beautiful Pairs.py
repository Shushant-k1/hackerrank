# just check no of common elements in two array
# substract one if array size and no of array elemsnts are equal because u have to change atleast one elemnet in the array
# else return coomon + 1
def beautifulPairs(A, B):
    # Write your code here
    d = {}
    for i in range(len(A)) :
        if A[i] in d :
            d[A[i]] += 1
        else :
            d[A[i]] = 1
    ans = 0
    for i in range(len(B)) :
        if B[i]  in d :
            if d[B[i]] > 0 :
                ans = ans + 1
                d[B[i]] -= 1
        
    if ans == len(A) :
        return ans - 1
    return ans + 1                
