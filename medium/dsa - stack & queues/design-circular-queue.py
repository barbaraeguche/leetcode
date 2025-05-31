# name: 622. design circular queue
# link: https://leetcode.com/problems/design-circular-queue

# solution #
class MyCircularQueue:
	
	def __init__(self, k: int):
		self.size = self.headIndex = 0
		
		self.capacity = k
		self.queue = [None] * self.capacity
	
	def enQueue(self, value: int) -> bool:
		if self.isFull():
			return False
		
		# modulo to prevent out of bounds error
		emptySlot = (self.headIndex + self.size) % self.capacity
		self.queue[emptySlot] = value
		
		# increment the count of queue items
		self.size += 1
		return True
	
	def deQueue(self) -> bool:
		if self.isEmpty():
			return False
		
		# reset the slot back to None
		self.queue[self.headIndex] = None
		
		# modulo to prevent out of bounds error
		self.headIndex = (self.headIndex + 1) % self.capacity
		# decrement the count of queue items
		self.size -= 1
		
		return True
	
	def Front(self) -> int:
		if self.isEmpty():
			return -1
		return self.queue[self.headIndex]
	
	def Rear(self) -> int:
		if self.isEmpty():
			return -1
		
		rearIndex = (self.headIndex + self.size - 1) % self.capacity
		return self.queue[rearIndex]
	
	def isEmpty(self) -> bool:
		return self.size == 0
	
	def isFull(self) -> bool:
		return self.size == self.capacity
