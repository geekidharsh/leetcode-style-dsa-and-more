"""meta, data engineer
Find the key of the highest value in a given dictionary. If there is 
more than one record with the highest value, sort their keys in ascending order and return the first.
hint: 
To find the key of the highest value in a given dictionary, if there is more than one 
record with the highest value, sort the keys in ascending order and return the first one. 

Input: {"date": 3, "apple": 5, "banana": 2, "cherry": 5}
Output: "apple"
"""

def key_of_highest_value(dct):
    """ 
    :type dct: dict
    :rtype: str
    """
    # get all values and find max
    max_val = max(dct.values())

    # list to gather all keys matching the max val
    matching_keys = []
    
    for key, val in dct.items():
        if val == max_val:
            matching_keys.append(key)
    
    # if more than one key, sort otherwise dont
    if len(matching_keys) > 1:
        matching_keys.sort()

    return matching_keys[0]