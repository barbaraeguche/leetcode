# name: 225. implement stack using queues
# link: https://leetcode.com/problems/implement-stack-using-queues

# solution #
class MyStack:

    def __init__(self):
        self.stack = []
        self.top_value = None
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top_value = x
    
    def pop(self) -> int:
        popped = self.stack.pop()
        self.top_value = self.stack[-1] if self.stack else None
        return popped
    
    def top(self) -> int:
        return self.top_value
    
    def empty(self) -> bool:
        return len(self.stack) == 0