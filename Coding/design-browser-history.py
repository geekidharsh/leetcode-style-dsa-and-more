# Design Browser History

# create a doubly linked list data structure
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr = ListNode(homepage)


    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr and steps:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.prev.val

        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr and steps:
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
homepage = 'google.com'
tab = BrowserHistory(homepage)
tab.visit('leetcode.com')
tab.visit('yahoo.com')
tab.back(4)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)