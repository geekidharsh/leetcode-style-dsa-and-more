# temp script file for revision

strs = ["eat","tea","tan","ate","nat","bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]

def anagram(strs):
    groups = {}
    for i in range(len(strs)): # O(n)
        temp = ''.join(sorted(strs[i])) #n^2log(n)
        if temp in groups:
            groups[temp].append(strs[i])
        else:
            groups[temp] = [strs[i]]
    
    return groups.values()

print(anagram(strs))               