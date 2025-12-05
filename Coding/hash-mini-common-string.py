# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and 
# list2[j] then i + j should be the minimum value among all the other common strings.

# company: facebook / meta

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]


def miniCommonStringSum(list1, list2):
    # find common comments using set intersection
    # can also do set1 & set2 to find common
    common_comments = set(list1).intersection(set(list2))
    
    # use this to store all common comments and sum of index
    common_comment_map = {}

    for idx, item in enumerate(list1):
        if item in common_comments:
            common_comment_map[item] = idx
    
    for idx, item in enumerate(list2):
        if item in common_comments:
            common_comment_map[item] += idx
    
    min_val = min(common_comment_map.values())

    # store result, could be more than one
    result = []

    for key, val in common_comment_map.items():
        if min_val == val:
            result.append(key)
    return result


miniCommonStringSum(list1, list2)