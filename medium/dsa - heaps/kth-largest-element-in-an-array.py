# name: 215. kth largest element in an array
# link: https://leetcode.com/problems/kth-largest-element-in-an-array

# solution #
import heapq as hq

class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		heap = []
		
		for num in nums:
			hq.heappush(heap, num)
		
		return hq.nlargest(k, heap)[-1]
