# name: 703. kth largest element in a stream
# link: https://leetcode.com/problems/kth-largest-element-in-a-stream

# solution #
import heapq as hq

class KthLargest:
	
	def __init__(self, k: int, nums: List[int]):
		self.k, self.heap = k, nums
		# heapify
		hq.heapify(self.heap)
		
		# keep heap in range k
		while len(self.heap) > self.k:
			hq.heappop(self.heap)
	
	def add(self, val: int) -> int:
		hq.heappush(self.heap, val)
		
		# keep heap in range k
		while len(self.heap) > self.k:
			hq.heappop(self.heap)
		
		return self.heap[0]
	