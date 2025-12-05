# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]



# solution:
# 1. for a given n, there are as many open parentheses as there are closed parentheses:
# 	i.e: when 0 open parentheses, then 0 closed parentheses
# 2. if open > close then return
# 3. if open = 0 then add open parentheses
# 4. if close = 0 then add close parentheses




def generate_parenthesis(n):
	result = []
	def gen(o,c,s): #gen(open, close, '')
		print('open {}, close {}, string: {}'.format(o, c, s))
		if o == 0 and c == 0:
			result.append(s)
		if o > c: #when there is a mismatch between o and c, recursion will stop
			return
		if o == 0:
			gen(o,c-1,s+')')
		else:
			gen(o-1, c, s+'(')
			gen(o,c-1, s+')')
	gen(n,n,'')
	return result


print(generate_parenthesis(3))


# Pass
# n = 3

# (
# ((
# (((
# ((()
# ((())
# ((()))
# result = ['((()))']
# (







