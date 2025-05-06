# name: 628. maximum product of three numbers
# link: https://leetcode.com/problems/maximum-product-of-three-numbers

# solution #
class Solution:
	def maximumProduct(self, nums: List[int]) -> int:
		if len(nums) == 3:
			return math.prod(nums)
		
		two_small_one_large = math.prod(
			(heapq.nsmallest(2, nums) + heapq.nlargest(1, nums))
		)
		three_large = math.prod(
			heapq.nlargest(3, nums)
		)
		
		return max(two_small_one_large, three_large)
	