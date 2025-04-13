# name: 977. squares of a sorted array
# link: https://leetcode.com/problems/squares-of-a-sorted-array

# solution #
class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		for i, num in enumerate(nums):
			nums[i] = num ** 2
		
		# reverse arr
		nums.sort()
		
		return nums