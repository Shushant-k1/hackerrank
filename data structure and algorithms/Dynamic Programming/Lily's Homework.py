# min swaps to sort array
def getWays(arr, goal):
    arr_loc = {n:i for i, n in enumerate(arr)}
    swaps = 0
    for i, n in enumerate(arr):
        if goal[i] != n:
            # swap with correct number at that index of goal
            temp = n
            arr[i] = arr[arr_loc[goal[i]]]
            arr[arr_loc[goal[i]]] = temp
            # update changed array locs
            arr_loc[temp] = arr_loc[goal[i]]
            arr_loc[goal[i]] = i
            swaps += 1
    return swaps
def lilysHomework(arr):
    return min(getWays(arr.copy(), sorted(arr)), getWays(arr.copy(), sorted(arr, reverse=True))) 
