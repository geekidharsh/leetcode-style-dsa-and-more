"""
Determine if an array is monotonic. A monotonic array has values strictly increasing or decreasing, but not both.
Input: [7, 5, 3, 3, 1]
Output: true
Description: This test case checks if the function correctly identifies a monotonic decreasing 
array which includes duplicate values.
"""
# data engineer, meta


lst = [1, 2, 3, 4, 5]
lst1 = [5,4,3,2,1]

def is_monotonic(lst):
    """
    :type lst: List[int]
    :rtype: bool
    """
    # check for increasing and decreeasing
    inc_stack = []
    dec_stack = []
    
    for num in lst:
        # if stack is non empty or stack[-1] is more than num
        if inc_stack and inc_stack[-1] > num:
            break
        inc_stack.append(num)
    
    for num in lst:
        if dec_stack and dec_stack[-1] < num:
            break
        dec_stack.append(num)

    # return true if either inc or decreeasing is_monotonic stack    
    return len(inc_stack) == len(lst) or len(dec_stack) == len(lst)

assert is_monotonic(lst) == True
assert is_monotonic(lst1) == True