# name: 3066. minimum operations to exceed threshold value ii
# link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

# solution #
import heapq as hq

class Solution:
	def minOperations(self, nums: List[int], k: int) -> int:
		count, heap = 0, []
		
		for num in nums:
			hq.heappush(heap, num)
		
		# check if the minimum value is >= k
		while len(heap) >= 2 and heap[0] < k:
			# keep track of operations
			count += 1
			
			x, y = hq.heappop(heap), hq.heappop(heap)
			
			# perform action
			value = min(x, y) * 2 + max(x, y)
			# insert back into heap
			hq.heappush(heap, value)
		
		return count
