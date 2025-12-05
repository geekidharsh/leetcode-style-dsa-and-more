import re
s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    # using regex replace all non alphanumeric with "" and additionally 
    # make s lower case

    # s = re.sub("[^a-z|^0-9]","",s.lower())
    beg = 0
    end = len(s) - 1

    # going left and right with two pointers, compare for equality
    while beg < end:
        if not s[beg].alnum():
            beg += 1
        elif not s[end].alnum():
            end -= 1

        elif not s[beg].lower() == s[end].lower():
            return False
        else:
            beg += 1
            end -= 1
    return True

print(isPalindrome(s))


# another way

def isPalindromeApproachTwo(s):
    filtered_s = []
    for char in s:
        if char.isalnum():
            filtered_s.append(char.lower())
    beg = 0
    end = len(filtered_s) - 1
    while beg < end:
        if not filtered_s[beg] == filtered_s[end]:
            return False
        else:
            beg += 1
            end -= 1
    return True

print(isPalindromeApproachTwo(s))