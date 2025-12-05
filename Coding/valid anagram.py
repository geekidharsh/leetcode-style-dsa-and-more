# valid anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true


def isAnagram(s, t):
    s_map = {} #k,v pair of char in s
    for i in s:
        if i not in s_map:
            s_map[i] = 1
        else:
            s_map[i] += 1

    for i in t:
        if i not in s_map: #if i not in s_map then false
            return False
        else:
            s_map[i] -= 1
            
    # finally get the output in a set()
    final_output = set(s_map.values())

    # if str is anagram then only one unique item of value 0 should be there    
    if len(final_output) == 1 and 0 in final_output:
        return True
    else:
        return False

s = "anagram"
t = "nagaram"

isAnagram(s,t)