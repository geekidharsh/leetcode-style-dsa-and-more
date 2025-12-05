# Logger Rate Limiter
# Design a logger system that receives a stream of messages along with their timestamps.
# Each unique message should only be printed at most every 10 seconds 
# (i.e. a message printed at timestamp t will prevent other identical messages 
# from being printed until timestamp t + 10).

# All messages will come in chronological order. Several messages may arrive at the 
# same timestamp.

# ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]

inp = [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]

class Logger:
    
    def __init__(self):
        self.msg_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str):
        if message not in self.msg_map:
             self.msg_map[message] = timestamp
             return True
        else: 
            if self.msg_map[message] + 10 >= timestamp:
                self.msg_map[message] = timestamp
                return True
            else:
                return False    

        

inp = [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
        
msg_log = Logger()
print(msg_log.shouldPrintMessage(1, 'foo'))
print(msg_log.shouldPrintMessage(5, 'foo'))
print(msg_log.shouldPrintMessage(11, 'foo'))

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)