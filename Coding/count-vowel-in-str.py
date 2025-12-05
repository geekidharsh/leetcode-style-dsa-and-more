# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all 
# five vowels present in it.

# Given a string word, return the number of vowel substrings in word.
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"

# complexity o(n^2)
# create a set for all vowels in word, so they are unique char
# iterate word, for any time there is a vowel, create a temp pointer from i+1 until it breaks
# if all vowels are found, current will be 5 len, update result. 
# reset current set

def countVowelInStr(word):
    result = 0 
    current = set()
    vowels = 'aeiou'

    for i in range(len(word)):
        if word[i] in vowels:
            current.add(word[i])
            for j in range(i+1, len(word)):
                if word[j] in vowels:
                    current.add(word[j])
                else:
                    break
                if len(current) == 5:
                    result += 1
        current = set()
    return result