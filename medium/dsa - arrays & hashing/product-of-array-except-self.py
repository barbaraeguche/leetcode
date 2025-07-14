# name: 238. product of array except self
# link: https://leetcode.com/problems/product-of-array-except-self

# solution #
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		length = len(nums)
		
		left, right = [1] * length, [1] * length
		
		for i in range(1, length):
			left[i] = left[i-1] * nums[i-1]
			right[-i-1] = right[-i] * nums[-i]
		
		for i in range(length):
			left[i] = left[i] * right[i]
		
		return left

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""