# name: 281. zigzag iterator
# link: https://leetcode.com/problems/zigzag-iterator

# solution #
class ZigzagIterator:
	def __init__(self, v1: List[int], v2: List[int]):
		self.queue = deque()
		self.vectorMap = {}
		
		# add vectors to hash map
		if v1:
			self.queue.append(1)
			self.vectorMap[1] = deque(v1)
		if v2:
			self.queue.append(2)
			self.vectorMap[2] = deque(v2)
	
	def next(self) -> int:
		current = self.queue.popleft()
		value = self.vectorMap[current].popleft()
		
		# if vector still has elements
		if self.vectorMap[current]:
			self.queue.append(current)
		
		return value
	
	def hasNext(self) -> bool:
		return len(self.queue) > 0

"""
time complexity:
- O(1)

space complexity:
- O(n * k); n is the number of vectors, k is the length of each queue
"""