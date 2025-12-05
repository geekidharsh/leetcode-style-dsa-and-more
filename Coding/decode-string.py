# neetcode all 
# stack and recursive 
# bloomberg, amazon, google, tiktok, uber

# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being 
# repeated exactly k times. Note that k is guaranteed to be a positive integer.

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# approach
# using stack keep pushing until a closing bracket is found - nested or otherwise
# then keep poping to get the char, then get the k number
# make resulting string
# time is o(n), space is o(n)

def decodeString(s):
    """
    given a string nested in k[encoded] structure
    return the decoded string
    """
    stack = []
    for i in range(len(s)):
        print(stack)
        if s[i] != ']':
            stack.append(s[i])
        else:
            result = ""
            while stack[-1] != '[':
                result = stack.pop() + result   # stack.pop() + result so that the result arranges in right order
            stack.pop()                         # finally remove '[' itself

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k        
            stack.append(int(k) * result)       # append stack with new formed substr 
    # finally, join the entire stack to get result
    return "".join(stack)


s= "3[a2[c]]"
print(decodeString(s))













