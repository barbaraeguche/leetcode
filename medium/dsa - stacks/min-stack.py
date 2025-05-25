# name: 155. min stack
# link: https://leetcode.com/problems/min-stack

# solution #
class MinStack:
	
	def __init__(self):
		self.stack = []
	
	def push(self, val: int) -> None:
		if self.stack:
			minval = min(self.stack[-1][0], val)
		else:
			minval = val
		
		# store as (min, val)
		self.stack.append((minval, val))
	
	def pop(self) -> None:
		self.stack.pop()
	
	def top(self) -> int:
		return self.stack[-1][1]
	
	def getMin(self) -> int:
		return self.stack[-1][0]
