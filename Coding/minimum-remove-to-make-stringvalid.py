# meta 100
# # Minimum Remove to Make Valid Parentheses

# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any 
# positions ) so that the resulting parentheses string is valid and return any valid string.

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


s = "lee(t(c)o)de)"

def minRemoveToMakeValid(s):
    result = []
    count = 0
    
    for ch in s:
        if ch not in ['(', ')']:
            result.append(ch)
        # keep updating count of open and close
        if ch == '(':
            result.append(ch)
            count += 1 #update
        if ch == ')' and count > 0:
            result.append(ch)
            count -= 1 #update
    
    # Second pass: remove extra opening parentheses without using 'continue'
    final_result = []
    open_to_remove = count  # Track extra '(' to remove

    for char in reversed(result):
        if char == '(' and open_to_remove > 0:
            open_to_remove -= 1  # Skip adding this '(' in final
        else:
            final_result.append(char)
    
    return ''.join(reversed(final_result))

    print(result, count, ''.join(result))
    return ''.join(result)




minRemoveToMakeValid(s)