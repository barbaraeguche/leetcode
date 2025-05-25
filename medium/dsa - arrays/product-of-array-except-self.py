# name: 238. product of array except self
# link: https://leetcode.com/problems/product-of-array-except-self

# solution #
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		left, right = [1] * len(nums), [1] * len(nums)
		
		# start with 1 at both ends, then [0] val at idx 1
		for i, n in enumerate(nums[:-1], 1):
			left[i] = nums[i-1] * left[i-1]
			right[-i-1] = nums[-i] * right[-i]
		
		# store the calculation in the left array
		for i, n in enumerate(left):
			left[i] = left[i] * right[i]
		
		return left
	