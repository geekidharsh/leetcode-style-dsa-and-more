# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

 

# Example 1:

# Input: order = "cba", s = "abcd"

# Output: "cbad"


from collections import Counter

def customSortString(order, s):
    # intuition
    # need is to built a new output of s but follow order's order for all char in order
    # we use a hashmap to get count of all char in s
    # built result str 
    s_count = Counter(s)
    result = ''

    for ch in order:
        if ch in s_count:
            temp_char = ch * s_count[ch]
            result += temp_char
            # delete char map from s_count once it's been added to result
            del s_count[ch]
        
    # finally append to the result all remaining char in s_count
    for char in s_count:
        temp_char = char * s_count[char]
        result += temp_char
    
    return result

# test
order = "cba"
s = "abcd"