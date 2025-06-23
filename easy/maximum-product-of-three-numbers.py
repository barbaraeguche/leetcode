# name: 628. maximum product of three numbers
# link: https://leetcode.com/problems/maximum-product-of-three-numbers

# solution #
import heapq as hq

class Solution:
	def maximumProduct(self, nums: List[int]) -> int:
		if len(nums) == 3:
			return math.prod(nums)
		
		two_small_one_large = math.prod((hq.nsmallest(2, nums) + hq.nlargest(1, nums)))
		three_large = math.prod(hq.nlargest(3, nums))
		
		return max(two_small_one_large, three_large)
	