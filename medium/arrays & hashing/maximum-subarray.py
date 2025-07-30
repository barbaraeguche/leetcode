# name: 53. maximum subarray
# link: https://leetcode.com/problems/maximum-subarray

# solution #
class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		currSum = maxSum = nums[0]
		
		for num in nums[1:]:
			# maximum of num or continuous window
			currSum = max(num, currSum + num)
			maxSum = max(maxSum, currSum)
		
		return maxSum

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""