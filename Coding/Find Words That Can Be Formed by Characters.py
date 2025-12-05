# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars 
# (each character can only be used once).

# Return the sum of lengths of all good strings in words.

#  Example 1:

words = ["cat","bt","hat","tree"]
chars = "atach"

# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" 
# so the answer is 3 + 3 = 6.

def count_chars(words, chars):
    result = 0
    for w in words:
        for ch in chars:
            print(w, words.count(w), ch, chars.count(ch))
    

count_chars(words, chars)