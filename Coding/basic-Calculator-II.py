# Basic Calculator II

# Input: s = "3+2*2"
# Output: 7

s = " 30+2 *2 "

def calculator(s):
    result = []
    i = 0
    while i < len(s):
        print(result)
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            result.append(num)
        elif s[i] in '+-/*':
            if s[i] == '+':
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 + num2)
            i += 1
        else:
            i += 1
        
    return result

calculator(s)