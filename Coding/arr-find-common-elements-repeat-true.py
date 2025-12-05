"""

meta, data engineer
arr, hashmap, collections

Find common elements in 2 given lists and return all aspects even if they are repeated.
Constraints
The input variables list1 and list2 should be of type List[int].
The input lists can have any length.
The elements in the input lists can be repeated.
The elements in the input lists can be in any order.
The input lists can contain both positive and negative integers.
The input lists can contain zero as an element.
The input lists can be empty.

Input: {"list1": [1, 2, 2, 3, 4], "list2": [2, 2, 3, 3, 4, 4]}
Output: [2, 2, 3, 4]
Description: This test case checks the function with two lists containing repeated integers. 
The common elements, including their repetitions, should be [2, 2, 3, 4].
"""

input = {'list1': [1, 2, 2, 3, 4],  'list2': [2, 2, 3, 3, 4, 4]}

import collections
def common_elements(input):
    list1 = input['list1']
    list2 = input['list2']
    
    num1_count =  collections.Counter(list1)
    num2_count = collections.Counter(list2)
    
    result = []
    for num in num1_count:
        if num in num2_count:
            # if number exists, get minimum of the appearances that would make them common in both
            com_freq = min(num1_count[num], num2_count[num])
            output = [num] * com_freq
            result.extend(output)
    return result

common_elements(input)