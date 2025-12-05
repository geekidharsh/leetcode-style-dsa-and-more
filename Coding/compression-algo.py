# 
# Let's assume that I have some data in a table and it looks like this:
# 
# [
# ["a","a","b","b","c","a"],
# ["a","a","b","b","c","a"],
# ["a","b","b","c","c","a"],
# ["a","b","b","c","c","c"],
# ["a","b","b","c","c","c"],
# ]
# 
# You can think of the data above as being a table, where each element in the first list is a row (i.e., you basically have a list of rows)
# 
# Imagine that the table is very very large, and I would like to compress this data before transmitting it over the network.
# 
# Scenario 1: Let's assume that we care about preserving the order in this data.
# 
# Scenario 2: Let's assume that we don't care about preserving the order in the data. 
# 
def compression(alist):
    str_list = ['aabbca']
    for row in alist:
        item = ''.join(row)
        str_list.append(item)

