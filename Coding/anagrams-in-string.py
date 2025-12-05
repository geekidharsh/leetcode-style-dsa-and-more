from collections import Counter

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]



s = "cbaebabacd"
p = "abc"


def anagramsInAString(s,p):

    # len
    M = len(p)
    N = len(s)

    # not sure about performance
    map_p = Counter(p)
    map_s = Counter(s[:M-1]) # pick first two elements initially
    print(map_s)

    output = []

    # o(n) where N is the longer string, only takes one pass.
    for i in range(M-1, N):

        # diff between i and len of p will give us starting index
        # and proceed in increments until the end of N
        start = i - (M-1)

        # add the last item to the map to maintain range start, i
        map_s[s[i]] += 1
        print(map_s, map_p)
        if map_s == map_p:
            output.append(start)
        
        # after comparison reset the counter from the starting index
        map_s[s[start]] -= 1

        # if starting counter is 0, no need to maintain the key, so pop it out
        if map_s[s[start]] == 0:
            map_s.pop(s[start])
    print(output)

    return output


anagramsInAString(s,p)