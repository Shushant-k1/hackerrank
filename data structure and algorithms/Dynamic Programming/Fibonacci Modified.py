def fibonacciModified(t1, t2, n):
    # Write your code here
    for i in range(n-1):
        t1,t2=t2,t1+(t2*t2)
    return t1
    
