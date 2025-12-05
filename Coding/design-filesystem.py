# doordash, leetcode medium
# Implement the FileSystem class:
# You are asked to design a file system that allows you to create new paths and associate 
# them with different values.
# The format of a path is one or more concatenated strings of the form: 
# / followed by one or more lowercase English letters. 
# For example, "/leetcode" and "/leetcode/problems" are valid paths 
# while an empty string "" and "/" are not.

# approach: 
# use a trie ds to store values in memory efficiently
# traversing is the complicated part here, need to revise

class FileSystem:

    def __init__(self):
        self.end = 'end'
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        node = self.trie
        part = path.split('/')
        
        for i in range(1, len(part)):
            
            if i == len(part) - 1:
                # we reached the end of parts
                if part[i] in node:
                    # last item is in node then, path already exist
                    return False
                
                node[part[i]] = {self.end: value}
                return True
            
            if part[i] not in node:
                return False
            # keep going to the next item by updating node with ith part
            node = node[part[i]]        

    def get(self, path: str) -> int:
        node = self.trie
        parts = path.split('/')
        
        for idx in range(1, len(parts)):
            if parts[idx] not in node:
                return -1


            # keep going to the next item by updating node with ith part            
            node = node[parts[idx]]
        
        return node[self.end]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)