# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

s = "foo"
t = "bar"

def isIsomorphic(s, t) -> bool:
    # useless question but common in interviews
    # clever use of zip is needed
    s = set(s)
    t = set(t)
    if len(s) == len(t) == len(zip(s, t)):
        return True
    else:
        return False

assert isIsomorphic(s, t) == False