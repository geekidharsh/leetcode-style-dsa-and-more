"""
You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates 
that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

    """
# approach 1, greedy: 
# easy to understand, fast but will fail for some account balancing. start with this

def minTransfers(transactions: List[List[int]]) -> int:
    # get group of debt by user
    balances = defaultdict(int)
    for frm, to, amount in transactions:
        balances[frm] -= amount
        balances[to]  += amount

    # remove any user with 0 balance, since those don't need to be settled
    debt = [i for i in balances.values() if i != 0]
    # print(debt)

    # greedy approach, settle largest debitor with largest creditor
    debt.sort()
    print(debt)
    count = 0
    i = 0
    j = len(debt) - 1

    while i < j:
        settle_amt = min(-debt[i], debt[j])
        debt[i] += settle_amt
        debt[j] -= settle_amt
        print(debt)
        # we update transaction count since one transaction just occurred
        count += 1
        # now, one or both maybe at 0, we check and move pointers accordingly
        if debt[i] == 0:
            i += 1
        if debt[j] == 0:
            j -= 1

    return count