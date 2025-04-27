# name: 704. binary search
# link: https://leetcode.com/problems/binary-search

# solution #
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1
		
		while l <= r:
			m = (l + r) // 2
			num = nums[m]
			
			if num == target:
				return m
			
			if num < target:
				l = m + 1
			elif num > target:
				r = m - 1
		
		return -1
	