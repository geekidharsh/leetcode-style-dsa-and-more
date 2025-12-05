prices = [7,1,5,3,6,4]

def buyAndsellStock(prices):
    i = 0
    j = len(prices) - 1
    buy = prices[i] #2
    sell = prices[j] #1
    profit = 0

    while i < j:
        if prices[i+1] < buy:
            buy = prices[i+1]
        
        if prices[j-1] > sell:
            sell = prices[j-1]
        i += 1
        j -= 1
        profit_today = sell - buy
        if profit_today > profit:
            profit = profit_today 
    return profit

print(buyAndsellStock(prices))

assert buyAndsellStock([7,1,5,3,6,4]) == 5
assert buyAndsellStock([2,1]) == 0