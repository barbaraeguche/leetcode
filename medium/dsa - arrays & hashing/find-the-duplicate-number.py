# name: 287. find the duplicate number
# link: https://leetcode.com/problems/find-the-duplicate-number

# solution #
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		for num in nums:
			idx = abs(num) - 1
			
			# has visited
			if nums[idx] < 0:
				return abs(num)
			
			# mark as negative
			nums[idx] *= -1
		
		return -1
