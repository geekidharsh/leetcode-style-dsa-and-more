# Given an array of strings, group anagrams together.Input: 

# ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(arr):
	group = {}
	for i in range(0,len(arr)):
		# sorting every item in arr.
		# if new item is found adding it to the dict
		# if sorted item exists as a key in dict, then update key's list value with arr item's index position

		s_item = ''.join(sorted(arr[i]))
		if s_item in group:

			group[s_item].append(i)
		else:
			group[s_item] = [i]

	return group


# complexity: 
print(group_anagrams(arr))