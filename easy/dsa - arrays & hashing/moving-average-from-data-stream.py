# name: 346. moving average from data stream
# link: https://leetcode.com/problems/moving-average-from-data-stream

# solution #
class MovingAverage:
	
	def __init__(self, size: int):
		self.idx = self.total = self.capacity = 0
		
		# initialize array
		self.size = size
		self.nums = [None] * self.size
	
	def next(self, val: int) -> float:
		# calculate current index
		idx = self.idx % self.size
		
		if self.nums[idx] is not None:
			num = self.nums[idx]
			
			# remove from moving average
			self.total -= num
			
			# update index
			self.idx = idx + 1
		else:
			# increment index
			self.idx += 1
			self.capacity = self.idx
		
		# replace old value; add to moving average
		self.nums[idx] = val
		self.total += val
		
		# average is total / capacity
		dividend, divisor = self.total, self.capacity
		
		return dividend if divisor - 1 == 0 else dividend / divisor

"""
time complexity:
- O(n) for init
- O(1) for next

space complexity:
- O(n)
"""