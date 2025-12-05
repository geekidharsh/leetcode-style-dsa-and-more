# Valid Word Abbreviation
# A string can be abbreviated by replacing any number of non-adjacent, 
# non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)

# Given a string word and an abbreviation abbr, return whether the string 
# matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true

word = "internationalization"
abbr = "i12iz4n"

def validWordAbbr(word, abbr):

    w = len(word)
    a = len(abbr)

    i = j = 0
    while i < w and j < a:
        if word[i] == abbr[j]:
            i += 1
            j += 1
        elif abbr[j] == '0': #solving the edge case for leading 0
            return False
        elif abbr[j].isdigit(): #if reach a digit, then start from there until all digits are iterated
            temp = j
            while temp < a and abbr[temp].isdigit():
                temp += 1
            i += int(abbr[j:temp]) #get the values and add them to i counter
            j = temp #resume j from temp index
        else:
            return False
    return i == w and j == a

word = "internationalization"
abbr = "i12iz4n"

print(validWordAbbr(word, abbr))