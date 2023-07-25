class MyQueue:

    def __init__(self):
        self.main = []
        self.backup = []
        

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        l = len(self.main)-1
        while l > 0:
            c = self.main[-1] 
            self.backup.append(c)
            self.main.pop()
            l-= 1
        # This should run until the last one
        r = self.main[-1]
        self.main.pop()
        # Now we need to repopulate main
        while self.backup:
            c = self.backup[-1]
            self.main.append(c)
            self.backup.pop()
        return r

    def peek(self) -> int:
        if self.main:
            return self.main[0]
        else:
            None
    def empty(self) -> bool:
        return not self.main
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()