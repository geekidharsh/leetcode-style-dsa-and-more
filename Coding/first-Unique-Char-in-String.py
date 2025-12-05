# First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return 
# its index. If it does not exist, return -1.
 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2


s = "leetcode"

def uniqueChar(s):
    #     trick is to count the number of char per alphabet
    #     then iterate from 0 index and return first occurance of char count == 1
    #     o(n) - two seperate iteration
    #     space: o(1) - input possibilities are limited to 26 letters only
        char_count = {}
        for i in range(len(s)):
            if s[i] not in char_count:
                char_count[s[i]] = 1
            else:
                char_count[s[i]] += 1
        
        for ind in range(len(s)):
            if char_count[s[ind]] == 1:
                return ind
        return -1


print(uniqueChar(s))