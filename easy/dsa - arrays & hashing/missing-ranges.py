# name: 163. missing ranges
# link: https://leetcode.com/problems/missing-ranges

# solution #
class Solution:
	def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
		# edge case: empty array
		if not nums:
			return [[lower, upper]]
		
		ranges = []
		
		# edge case: first missing range
		if nums[0] - lower >= 1:
			ranges.append([lower, nums[0] - 1])
		
		for i in range(1, len(nums)):
			num1, num2 = nums[i-1], nums[i]
			
			# lower and upper bounds between the numbers
			lowerBound, upperBound = num1 + 1, num2 - 1
			
			# error: not a missing range
			if lowerBound >= num2 or upperBound <= num1:
				continue
			
			# append to list
			ranges.append([lowerBound, upperBound])
		
		# edge case: last missing range
		if upper - nums[-1] >= 1:
			ranges.append([nums[-1] + 1, upper])
		
		return ranges

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""