# 921. Minimum Add to Make Parentheses Valid
# Medium

# 539

# 40

# Add to List

# Share
# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

# Example 1:

# Input: "())"
# Output: 1
# Example 2:

# Input: "((("
# Output: 3



def minAddToMakeValid(S):
    if len(S) <= 1000:
        prefix = 0
        balance = 0
        for i in S:
            if i == '(':
                balance += 1
            elif i == ')':
                balance -= 1
            if balance == -1:
                prefix += 1
                balance += 1
        return balance + prefix
    else:
        return -1



S = "()))(("

print(minAddToMakeValid(S))


