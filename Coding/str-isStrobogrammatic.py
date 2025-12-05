"""Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: num = "69"
Output: true"""

def isStrobogrammatic(self, num: str) -> bool:
    num_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    # also verify that the number reversed and mapped matches the original
    rotate_num = ''
    # num = 69
    for n in reversed(num): # 96
        if n not in num_map:
            return False
        rotate_num += num_map[n]
    # if rotate_num maps to original, return True
    return True if rotate_num == num else False

