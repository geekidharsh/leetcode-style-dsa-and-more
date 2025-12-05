# // Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

"""
leetcode hard. Linkedin, Meta, amazon, google, tiktok
Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

You must come up with a solution that supports O(1) for each top call and O(logn) for each other call."""


# Input: ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# Output: [null, null, null, null, 5, 5, 1, 5, 1, 5]

# approach using two stacks: works but is o(n) for popMax.

class MaxStackStandard:
    def __init__(self):
        self.stack = []
        self.max_vals = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.max_vals:
            val = max(self.max_vals[-1], x)
            self.max_vals.append(val)
        else:
            self.max_vals.append(x)


    def pop(self) -> int:
        # remove from top, keeping both stacks in sync
        val = self.stack.pop()
        self.max_vals.pop()
        return val

    def top(self) -> int:
        # get element at the top
        return self.stack[-1]


    def peekMax(self) -> int:
        # get max element
        return self.max_vals[-1]

    def popMax(self) -> int:
        # get max value
        val = self.peekMax()
        buffer = []
        while self.top() != val:
            temp = self.pop()
            buffer.append(temp)
        self.pop()
        
        # for loop will iterate from left to right, which we dont want
        # while pops from buffer in reverse. which is the correct ordering
        while buffer:
            self.push(buffer.pop())

        return val



class MaxStackOptimized:
    
    def __init__(self):
        pass
    
    def push(self, x:int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass
        

    def peekMax(self) -> int:
        pass

    def popMax(self) -> int:
        pass


# ---------
# test
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()