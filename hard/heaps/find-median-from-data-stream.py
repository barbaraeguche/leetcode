# name: 295. find median from data stream
# link: https://leetcode.com/problems/find-median-from-data-stream

# solution #
import heapq as hq

class MedianFinder:
	
	def __init__(self):
		self.maxheap = []
		self.minheap = []
	
	def addNum(self, num: int) -> None:
		hq.heappush(self.maxheap, -num)
		
		# do not defy the order
		if (
			self.maxheap and self.minheap and
			-self.maxheap[0] > self.minheap[0]
		):
			val = -hq.heappop(self.maxheap)
			hq.heappush(self.minheap, val)
		
		# handle uneven lengths
		if len(self.maxheap) > len(self.minheap) + 1:
			val = -hq.heappop(self.maxheap)
			hq.heappush(self.minheap, val)
		if len(self.minheap) > len(self.maxheap) + 1:
			val = -hq.heappop(self.minheap)
			hq.heappush(self.maxheap, val)
	
	def findMedian(self) -> float:
		if len(self.maxheap) > len(self.minheap):
			return -self.maxheap[0]
		if len(self.minheap) > len(self.maxheap):
			return self.minheap[0]
		
		return (-self.maxheap[0] + self.minheap[0]) / 2

"""
time complexity:
- addNum: O(log(n))
- findMedian: O(1)

space complexity:
- O(n)
"""