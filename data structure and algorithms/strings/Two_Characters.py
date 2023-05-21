from itertools import combinations
def alternate(s):
    comb = combinations(set(s), 2)
    max_one = 0
    for a, b in comb:
        stack = []
        check = True
        for i in s:
            if i in [a,b]:
                if not stack:
                    stack.append(i)
                elif(i == stack[-1]):
                    check = False
                    break
                else:
                    stack.append(i)
        if check and max_one < len(stack):
            max_one = len(stack)
    return max_one
