
def count_distinct_substr(inp):
    # using a set
    # set takes care of the distinctness, no need for counter etc
    substrs = set()
    n = len(inp)

    for i in range(n):
        # get all substr in s in the range of indices i to j where j starts at n, ends at i, decrements by -1
        for j in range(n,i,-1):
            substrs.add(inp[i:j])
    return len(substrs)


inp = 'aabbab'

count_distinct_substr(inp)