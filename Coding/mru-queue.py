# design a queue that returns most recently used item to the front
# bloomberg

class MRUQueue:

    def __init__(self, n: int):
        # initialize the list with n number of items
        self.data = list(range(1, n+1))
        

    def fetch(self, k: int) -> int:
        # print(self.data)

        # get the kth item and pop it from the list
        kth_item = self.data.pop(k-1)
        # print(self.data)
        # add kth item to the end
        self.data.append(kth_item)
        # return item while maintaining rest of the queue
        return self.data[-1]


queue = MRUQueue(8)
queue.fetch(3)