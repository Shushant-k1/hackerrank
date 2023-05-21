# program to check palindrome
def is_pal(s ) :
    low = 0
    high = len(s) - 1
    while low < high :
        if s[low] != s[high] :
            return False
        low += 1
        high -= 1
    return True
def palindromeIndex(s):
    # Write your code here
    if is_pal(s) :
        return -1
    i = 0
    j = len(s) - 1
    while i <  j :
      # if cureent elemnt is not equal then 
      # either we remove the last element or first lement
        if s[i] != s[j] :
          # making a new string
            p = s[:i] + s[i+1:]
            if is_pal(p): return i 
            p = s[:j] + s[j+1:]
            if is_pal(p): return j
        i += 1
        j -= 1
    return -1
    
