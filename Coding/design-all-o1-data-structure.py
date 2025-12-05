"""Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

linkedin, Meta, google - hard

test: 
Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]
"""

# works functionally but does not have the o(1) performance.
class AllOne:

    def __init__(self):
        self.string_map = {}

    def inc(self, key: str) -> None:
        if key in self.string_map:
            self.string_map[key] += 1
        else:
            self.string_map[key] = 1

    def dec(self, key: str) -> None:
        if key not in self.string_map:
            return
        self.string_map[key] -= 1
        if self.string_map[key] == 0:
            del self.string_map[key]

    def getMaxKey(self) -> str:
        if not self.string_map:
            return ""
        all_val = self.string_map.values()
        max_val = max(all_val)
        for key, val in self.string_map.items():
            if val == max_val:
                return str(key)

    def getMinKey(self) -> str:
        if not self.string_map:
            return ""
        
        all_val = self.string_map.values()
        min_val = min(all_val)
        for key, val in self.string_map.items():
            if val == min_val:
                return str(key)


