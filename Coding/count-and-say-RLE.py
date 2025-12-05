
from itertools import groupby
# this question is basically asking for generating run len encoding

"""
look at the group by usage below, then check main code
s = "3322251"
# groupby creates a tuple of groups and their values, group is it's own iterator. use a list of unpack
groups = groupby(s)
parts = []

for digit, group in groups:
    # store digit as key and group as value in map
    run = list(group)
    count = len(run)
    parts.append(str(count)+digit)

print(parts)
"""
from itertools import groupby

def next_term(s: str) -> str:
    parts = []
    for digit, group in groupby(s):
        run = list(group)
        count = len(run)
        parts.append(str(count) + digit)
    return "".join(parts)

def countAndSay(n: int) -> str:
    # each next term is built upon the prev one
    s = "1"
    for _ in range(n - 1):
        s = next_term(s)
    return s