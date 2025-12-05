

# hint: 
# most significant bit
# least significant bit


def pow(x,n):
    # long answer, would need revision
    def helper(a, b):
        # if power is 0, then answer is 1
        if b == 0:
            return 1
		# if power is 1 then answer is a
        if b == 1:
            return a
		# if power is negative, then we make power positive and use 1/a - as in maths
        if b < 0:
            return helper(1/a, -b)

		# finally after edge cases
        result = 1
        if b % 2 == 0:
			# if power is even, we get result for half - saving half of recursion 
   			# and multiply result by itself
            result = helper(a, b/2)
            return result * result
        else:
            # if power is odd, we get result for power - 1 and multipy with a
            result = helper(a, b - 1)
            return result * a
    
    return helper(x, n)
     
 



print(pow(2,6))


