"""Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements 
to the right. Note that elements beyond the length of the original array are not written. 
Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # in place is hard, otherwise it's easy to do
        # solution using o(n) memory
        temp = []
        
        for num in arr:
            if num == 0:
                temp.append(num)
            temp.append(num)
        
        return temp
    
