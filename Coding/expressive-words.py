# Expressive Words
# cisco, google

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", 
# but we cannot get "helloo" since the group "oo" has a size less than three. 
# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


s = "heeellooo"
words = ["hello", "hi", "helo"]

from collections import Counter

def expressiveWords(s, words):
    # get count of call chars in string
    s_count = Counter(s)
    ans = 0
    for word in words:
        # get count of all char in each word
        w_count = Counter(word)
        if w_count.keys() == s_count.keys(): #all characters exist in the word so proceed
            count = 0
            for ch in w_count:
                if w_count[ch] == s_count[ch] or (w_count[ch] < s_count[ch] and s_count[ch] >= 3): # this is based on the rule stated in the question
                    count += 1
                if count == len(w_count):
                    ans += 1
    return ans
        
            

print(expressiveWords(s, words))

