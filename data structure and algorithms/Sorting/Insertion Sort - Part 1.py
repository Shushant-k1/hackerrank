def insertionSort1(n, arr):
    # Write your code here
    for  i in range(n - 1 , 0 , -1 ) :
        if arr[i] < arr[i -1] :
            x = arr[i]
            p = i
            y = arr.copy()
            while x < arr[p -1] and p > 0:
                y[p] = y[ p - 1]
                print(*y)
                p -= 1
    arr.sort()
    print(*arr)
    
    
