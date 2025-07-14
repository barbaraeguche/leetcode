# name: 1480. running sum of 1d array
# link: https://leetcode.com/problems/running-sum-of-1d-array

# solution #
class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		for i in range(1, len(nums)):
			nums[i] += nums[i-1]
		
		return nums
	
"""
time complexity:
- O(n)

space complexity:
- O(1)
"""