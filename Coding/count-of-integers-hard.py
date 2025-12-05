# You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. 
# We denote an integer x to be good if:
# de shaw

# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum.
# Return the number of good integers. Since the answer may be large, return it modulo 109 + 7.

# Note that digit_sum(x) denotes the sum of the digits of x.

# Input: 
# num1 = "1", num2 = "12", min_sum = 1, max_sum = 8
# Output: 11
# Explanation: There are 11 integers whose sum of digits lies between 1 and 8 
# are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.
# Output: 11


# working solution but un optimized, 
# optimization using dp
def count_of_integers(num1, num2, min_sum, max_sum):
    def digit_sum(x):
        sum = 0
        while x > 0:
            sum += x % 10
            x = x // 10
        return sum

    counter = 0
    for i in range(int(num1), int(num2) + 1):
        i_sum = digit_sum(i)
        if min_sum <= i_sum <= max_sum:
            counter += 1
    return counter

num1 = "1"
num2 = "12"
min_sum = 1
max_sum = 8

print(count_of_integers(num1, num2, min_sum, max_sum))

