# input: list = [1, 2, 3, 4, 5], k = 2
# output: → [4, 5, 1, 2, 3]

# incomplete
# Given the head of a linked list, rotate the list to the right by k places.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Rotating the list to the right by k means:
        # The last k nodes move to the front.
        # The relative order of nodes stays the same.
        # now we have the head and tail of ll
        # next, connect tail to head, making it circular
        # this allows, to keep going forward from head
        # all we need to do is, walk few steps: steps = len_of_list - k + 1
        # if k > len(list) then k%len_of_list is exactly the same as walking k steps over
        
        if not head or not head.next or k == 0:
            return head
        
        list_len = 1
        tail = head
        while tail:
            tail = tail.next
            list_len += 1
        
        ol
        
        
        