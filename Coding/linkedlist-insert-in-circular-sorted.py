"""
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]

Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert 
a value insertVal into the list such that it remains a sorted circular list. The given node can be a 
reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""



class Solution:
    # approach: find all edge cases
    # easy once all is found:
    # if node is empty, 
    # if found a spot, 
    # if we reach the min or max edge of node
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # given head is empty
        if not head:
            newNode = Node(val=insertVal)
            newNode.next = newNode
            return newNode
        
        curr = head
        while curr:
            # val spot has been found, break it and jump to insertion
            if curr.val <= insertVal <= curr.next.val:
                break

            # keep moving
            curr = curr.next

            if curr.val > curr.next.val: # we are on the edge since it's circular and sorted
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break


            # we walked a full circle
            if curr == head:
                break


        # insertion
        newNode = Node(val=insertVal)
        newNode.next = curr.next
        curr.next = newNode
        return head
        
