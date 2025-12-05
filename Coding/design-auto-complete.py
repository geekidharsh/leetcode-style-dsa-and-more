"""
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end 
with a special character '#'). You are given a string array sentences and an integer array times both of length n 
where sentences[i] is a previously typed sentence and times[i] 
return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:
- The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
- The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). 
- If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
- If less than 3 hot sentences exist, return as many as you can.
- When the input is a special character, it means the sentence ends, and in this case, 
you need to return an empty list.

Implement the autocompletesystem class
pinterest, meta, linkedin / microsoft

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]

Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
"""

import heapq
from collections import defaultdict

# Define TrieNode structure
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.sentences = set()


# this is a simple autocorrect system without top 3 and frequency ability
# this system can store, lookup and return sentences matching a prefix

class AutocompleteSystem:
    def __init__(self, sentences):
        self.root = TrieNode()  # Root of the trie
        self.current_node = self.root  # Pointer to current node as we process input
        self.current_input = ""  # Stores the ongoing user input

        for sentence in sentences:
            self._add_sentence(sentence)

    def _add_sentence(self, sentence):
        # Adds a sentence into the trie, updating frequencies along the path
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create node if it doesn't exist
            node = node.children[char]
            node.sentences.add(sentence)
    
    def _lookup(self, prefix):
        """        
        Looks up all sentences with the given prefix
        returns sentences that match prefix otherwise {}"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return {}  # No match found
            node = node.children[char]
        #return node, node.children, node.sentences  # Return sentences that match the prefix
        return node.sentences
    
    def input(self, c):
        if c == '#':
            self._add_sentence(self.current_input)
            self.current_input = ""
            return []

        self.current_input += c
        return self._lookup(self.current_input)
        



# Your AutocompleteSystem object will be instantiated and called as such:
sentences = ["i love you", "island", "iroman", "i love leetcode"]
obj = AutocompleteSystem(sentences)

# Optional: expose lookup method if not public
print("Initial object:", obj)
print("Lookup 'ir':", obj._lookup("ir"))

print("Input 'i':", obj.input("i"))       # ["i love you", "i love leetcode", "iroman", "island"]
print("Input ' ':", obj.input(" "))       # ["i love you", "i love leetcode"]
print("Input 'isl':", obj.input("love"))       # ["i love you", "i love leetcode"]
print("Input '#':", obj.input("#"))       # []

print("Lookup 'i love':", obj._lookup("i love"))  # Should now inc de "i l"


# param_1 = obj.input(c)


# import sys
# s = sys.getsizeof(obj)
# print(s)