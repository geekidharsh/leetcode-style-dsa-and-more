# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# given two binary strings, add and return their sum as a binary string

a = "11"
b = "1"

# time: O(n,m)


def addBinary(a, b):
    # first we convert incoming string to a list so we can handle each element
    # then we convert to int at each iteration for a or b or carry
    # carry is the sum of a and b but if carry is 2, then we need to convert that to the nearest bin:
    # need to remember: result is the mod of carry
    # store carry // 2 to get absolute integers such as 0 or 1 instead of 0.5 in case of /


    a = list(a)
    b = list(b)
    carry = 0
    result = ""

    while a or b or carry:
        if a:
            carry += int(a.pop()) #to add, go from right to left so stack pop is useful
        if b:
            carry += int(b.pop())
        result += str(carry % 2)
        carry = carry // 2

    return result[::-1]

print(addBinary(a,b))




addBinary(a,b)