# name: 232. implement queue using stacks
# link: https://leetcode.com/problems/implement-queue-using-stacks

# solution #
class MyQueue:
	
	def __init__(self):
		self.queue = []
	
	def push(self, x: int) -> None:
		self.queue.append(x)
	
	def pop(self) -> int:
		popped = self.queue[0] if not self.empty() else None
		self.queue = self.queue[1:] if not self.empty() else None
		return popped
	
	def peek(self) -> int:
		return self.queue[0] if not self.empty() else None
	
	def empty(self) -> bool:
		return len(self.queue) == 0