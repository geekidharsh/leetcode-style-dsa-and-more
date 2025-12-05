# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # extract all values
        link_val = []

        curr = head
        while curr:
            link_val.append(curr.val)
            curr = curr.next
        
        # sort values
        link_val.sort()
        
        # create a new node and fill it up
        dummy = ListNode()
        curr = dummy
        for item in link_val:
            curr.next = ListNode(item)
            curr = curr.next
        
        return dummy.next


# follow up: do it in-place - Space: o(1)