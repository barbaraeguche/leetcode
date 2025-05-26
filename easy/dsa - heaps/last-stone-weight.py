# name: 1046. last stone weight
# link: https://leetcode.com/problems/last-stone-weight

# solution #
class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		heap = []
		
		# store in max-heap
		for stone in stones:
			heapq.heappush(heap, -stone)
		
		while len(heap) > 1:
			# first two largest
			l1, l2 = -heapq.heappop(heap), -heapq.heappop(heap)
			val = abs(l1 - l2)
			
			if l1 != l2:
				heapq.heappush(heap, -val)
		
		return 0 if not heap else -heap[0]
