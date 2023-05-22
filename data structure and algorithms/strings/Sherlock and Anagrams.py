def sherlockAndAnagrams(s):
    # Write your code here
    # Get all substrings as a list of sorted string
    sorted_substrings = []
    # Get count of each sorted substring
    count_dict = {}
    # generating all  sorted substring and add to dictionary 
    for i in range(len(s)):
        for j in range(i, len(s)):
            x = "".join(sorted(s[i : j + 1]))
            if x not in count_dict:
                count_dict[x] = 1
            else:
                count_dict[x] += 1      
            sorted_substrings.append(x)
    # Get count of anagram pairs
    #if count is greater than 1 for all combinations
    count = 0
    for x in count_dict:
        if count_dict[x] > 1:
            count += count_dict[x] * (count_dict[x] - 1) // 2
    return count
