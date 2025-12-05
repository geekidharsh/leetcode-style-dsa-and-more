#  Length of Last Word

# Given a string s consisting of some words separated by some number of spaces, 
# return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

s = "Hello world"
s1 = "fly me   to   the moon "
def lenOFLastStr(s):
    # time is o(n), space is o(n)
    s = s.split(' ')
    while s[len(s)-1].isalpha() == False:
        s.pop()
    return len(s[len(s)-1])

# def lenOfLastOpt(s):
#     last = len(s) -1
#     count = 0
#     while s[last] == ' ':
#         print(s[last])
#         last -= 1

        



print(lenOFLastStr(s1))
print(lenOfLastOpt(s))
