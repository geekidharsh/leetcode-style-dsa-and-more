# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a 
# subsequence and not a substring.

s = "harshvardhan" 

def longestSubstr(s):
    # store repeating char in a lookup table
    # use maxlen to keep a running max len from start
    # update start to the next char c when there is a duplicate 
    # char found in lookup
    
    lookup = {}
    maxlen = 0
    start = 0
    for i, c in enumerate(s):
        if c in lookup and start <= i:
            start = lookup[c] + 1
        else:
            maxlen = max(maxlen, i - start + 1)
        lookup[c] = i
    return maxlen

assert longestSubstr('abcabcbb') == 3
assert longestSubstr(s) == 6