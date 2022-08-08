#always we want to get a min value
# other option we can use priority queue

import heapq as heap
def cookies(k, A):
    # Write your code 
    heap.heapify(A)
    c=0
    for i in range(k):
        if A[0]>=k:
            return c
            break     
        else :
            if len(A)>1:
                a=heap.heappop(A)
                b=heap.heappop(A)
                heap.heappush(A,a+2*b)
                c=c+1
            else:
                return -1
    return -1
