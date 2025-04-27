# name: 35. search insert position
# link: https://leetcode.com/problems/search-insert-position

# solution #
class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1
		
		while l <= r:
			m = (l + r) // 2
			num = nums[m]
			
			if num < target:
				l = m + 1
			elif num > target:
				r = m - 1
			else: return m
		
		return l
	