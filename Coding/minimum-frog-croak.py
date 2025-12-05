# Output: 1 
# Explanation: One frog yelling "croak" twice.

# Example 2:
croakOfFrogs = "croakcroak"
croakOfFrogs1 = "crcoakroak"
# Output: 2 
# Explanation: The minimum number of frogs is two. 
# The first frog could yell "crcoakroak".
# The second frog could yell later "crcoakroak".

def minNumberOfFrogs(croakOfFrogs):
    """
    :type croakOfFrogs: str
    :rtype: int
    """
    c = r = o = a = k = 0
    result = -1
    active_frogs = 0
    for ch in croakOfFrogs:
        if ch == 'c':
            c = 1
            active_frogs += 1
        elif ch == 'r':
            r = 1
        elif ch == 'o':
            o = 1
        elif ch == 'a':
            a = 1
        elif ch == 'k':
            k = 1
            active_frogs -= 1
        result = max(active_frogs, result)
        # print(c, r, o, a, k)

    return result

print(minNumberOfFrogs(croakOfFrogs))
print(minNumberOfFrogs(croakOfFrogs1))
