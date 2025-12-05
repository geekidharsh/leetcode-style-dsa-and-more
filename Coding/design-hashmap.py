"""
Design a HashMap without using any built-in hash table libraries

To be specific, your design should include these functions:
put(key, value) : Insert a (key, value) pair into the HashMap. 
				  If the value already exists in the HashMap, update the value.

get(key): 	Returns the value to which the specified key is mapped, or -1 if this 
			map contains no mapping for the key.

remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

"""


class HashMap:
    """base class for HashMap"""
    
    def __init__(self):
        self.size = 1000
        self.arr = [None] * self.size


hash_obj = HashMap()
print(hash_obj.arr) 