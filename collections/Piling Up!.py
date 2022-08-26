# find peak element


T = int(input())
for _ in range(T):
    n = int(input())
    blocks = [int(x) for x in input().split()]
    answer = 'Yes'
    for i in range(1, n-1):
        if blocks[i] > blocks[i-1] and blocks[i] > blocks[i+1]:
            answer = 'No'
            break
    print(answer)
