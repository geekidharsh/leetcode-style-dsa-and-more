# Given a string s containing just the characters '(', ')', '{', '}', 
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# solution
# basically, this is a stack question.

# valid possibilities:
# every last item that is open should be the first one to close
# all brackets should be closed by the end of the list i.e the stack should be empty
# using a hashmap, map every closing parenthesis to an open parenthesis.

# time: o(n), space: o(n) for using a stack list, and a hashmap


s = "()[]{}"

def validParenthesis(s):
     # create a bracket map 
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in s:
        if char in bracket_map:
            # verify if stack is not empty and last item is 
            # the first opening bracket to be closed
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return False if stack else True

print(validParenthesis(s))