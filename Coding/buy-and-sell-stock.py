"""
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy 
before you sell."""


prices = [7,1,5,3,6,4]


def buyAndsellStock(prices):
    m = 0
    buy = prices[0]
    profit = 0
    for m in range(0,len(prices)):
        if buy > prices[m]:
            buy = prices[m]
        profit_today = prices[m] - buy
        profit = max(profit, profit_today)
        print('buy: {}, sell: {}, profit: {}'.format(buy, profit_today, profit))
    return profit

print(buyAndsellStock(prices))

assert buyAndsellStock([2,1]) == 0