# given a roman number - convert it to an integer

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# i will assume that the input string is always a roman numeral

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    s_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = []
    for symbol in s:
        if symbol in s_map:
            result.append(s_map[symbol])

    integer = 0
    i = 0
    for i in range(len(result)):
        if i+1 < len(result) and result[i] < result[i+1]:
            integer -= result[i]
        else:
            integer +=  result[i]
        i += 1

    return integer

s = "XIV"

# print(romanToInt(s))

# test
# print(romanToInt("III") == 3)
# print(romanToInt("MMMDCCXXIV") == 3724)
# print(romanToInt("IV") == 4)
# print(romanToInt("XIV") == 14)

#revised 
def romanToIntRevised(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    N = len(s) - 1
    while N >= 0:
        if N < len(s) - 1 and s[N] < s[N+1]:
            num -= roman[s[N]]
        else:
            num += roman[s[N]]
        N -= 1
    return num

n1 = romanToIntRevised("III")
n2 = romanToIntRevised("IV")
n3 = romanToIntRevised("XIV")
print(n1, n2, n3)