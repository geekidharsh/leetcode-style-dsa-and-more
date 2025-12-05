# palindrome-number.py

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

x = 121
def palindromeNumber(x):
    x = str(x)
    i = j = 0
    if x[0] =='-':
        return False
    else:
        while i < j:
            if x[i] == x[j]:
                i += 1
                j += 1
            else:
                return False
    return True