# name: 75. sort colors
# link: https://leetcode.com/problems/sort-colors

# solution #
class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		colors = [0, 0, 0]
		
		for num in nums:
			colors[num] += 1
		
		r, w, b = colors
		
		nums[:r] = [0] * r
		nums[r:r+w] = [1] * w
		nums[r+w:] = [2] * b
		