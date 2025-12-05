# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# amazon, bloomberg, google 
# Input: 
strs = ["flower","flow","flight"]
# Output: "fl"


# approach
# binary search approach, find the string with smallest length, 
# as this is the max prefix that there can be
# then we search only until the length of this shortest str for each str in strs
# if difference was found, shrink shortest str

def longestCommonPrefix(strs):
    # get the shortest string in list of strs
    shortest_str = min(strs, key=len)

    for idx, ch in enumerate(shortest_str):
        for i in strs:
            if i[idx] != ch:
                return shortest_str[:idx]
    return shortest_str

longestCommonPrefix(strs)