def highestValuePalindrome(s, n, k):
    # Write your code here
    # Check minimum number of changes needed to make it a palindrome
    min_count = 0
    min_change_index_list = []
    for i in range(n // 2):
        if s[i] != s[-1 - i]:
            min_count += 1
            min_change_index_list.append(i)
    if min_count > k:
        return "-1"

    # Make it with the minimum number of changes
    s = list(s)
    for i in min_change_index_list:
        s[i] = s[-1 - i] = max(s[i], s[-1 - i])

    # Return immediately if min_count == k
    if min_count == k:
        return "".join(s)

    # Make it with the maximum number of changes
    # Get index for making highest value
    max_change_index_list = []
    max_count = k - min_count
    for i in range(n // 2):
        if max_count == 0:
            break
        if s[i] != "9" and s[-1 - i] != "9":
            if i in min_change_index_list:
                max_count -= 1
                max_change_index_list.append(i)
            elif max_count >= 2:
                max_change_index_list.append(i)
                max_count -= 2
    for i in max_change_index_list:
        s[i] = s[-1 - i] = "9"
    if n % 2 == 1 and max_count > 0:
        s[n // 2] = "9"
    return "".join(s)
