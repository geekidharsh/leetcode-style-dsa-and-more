# linkedlist-intersection of two linkedin list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# linkedin, google, wells fargo

class Solution:
    # follow up: do it without using extra memory
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # using a hashset, store all nodes of A in a set, then iterate through B and check if node exists in set of A
        # time: o(m+n), space: o(n)
        node_map_a = set()
        temp = headA
        while temp:
            node_map_a.add(temp)
            temp = temp.next

        while headB:
            if headB in node_map_a:
                return headB
            headB = headB.next

        return None
        