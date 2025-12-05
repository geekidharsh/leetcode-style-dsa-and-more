
# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


class HashSet:
    # simplest form of hashset implementation
    # does not cover collision
    # but works fine
    def __init__(self) -> None:
        self.capacity = 100
        self.items = [None] * self.capacity
    
    def hash_helper(self, val):
        return val % self.capacity
    
    def add(self, val):
        loc = self.hash_helper(val)
        if not self.items[loc] == val:
            self.items[loc] = val
    
    def remove(self, val):
        loc = self.hash_helper(val)
        print(loc)
        if self.items[loc] == val:
            self.items[loc] = None
            print('Val {}, removed from set'.format(val))
    
    def contains(self, val):
        loc = self.hash_helper(val)
        if self.items[loc] == val:
            return True
        return False
            


custom_set = HashSet()
custom_set.add(5)
custom_set.add(50)
custom_set.add(22)
custom_set.remove(5)
custom_set.contains(22)
print(custom_set.items)