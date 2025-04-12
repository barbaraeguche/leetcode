# name: 283. move zeroes
# link: https://leetcode.com/problems/move-zeroes

# solution #
class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		idx = 0
		
		for num in nums:
			if num != 0:
				nums[idx] = num
				idx += 1
		
		while idx < len(nums):
			nums[idx] = 0
			idx += 1