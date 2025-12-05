# de shaw, amazon, meta, linkedin
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to 
any letters."""


def letter_comb_of_phone_number(digits):
    def backtrack(i, curStr):
        # print(output)
        if len(curStr) == len(digits):
            output.append(curStr)
            return
        
        for c in num_to_char_map[digits[i]]:
            backtrack(i+1, curStr+c)
    
    output = []
    num_to_char_map = {'2': 'abc', 
                '3': 'def', 
                '4': 'ghi', 
                '5': 'jkl', 
                '6': 'mno', 
                '7': 'pqrs', 
                '8': 'tuv', 
                '9': 'wxyz'}


    if digits:
        backtrack(0, '')

    return output

digits = "23"
print(letter_comb_of_phone_number(digits))