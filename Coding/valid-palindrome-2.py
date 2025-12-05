# Given a string s, return true if the s can be palindrome 
# after deleting at most one character from it.

# Input: s = "aba"
# Output: true

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

def validPalindrome(s):
    left = 0
    right = len(s) -1
    
    def isPalindrome(substr):
        start = 0
        end = len(substr) -1
        while start < end:
            if substr[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if isPalindrome(s[left:right - 1]) or isPalindrome(s[left+1:right]):
                return True
            else:
                return False
    return True



s = "abca"
print(validPalindrome(s))