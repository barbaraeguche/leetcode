# name: 918. maximum sum circular subarray
# link: https://leetcode.com/problems/maximum-sum-circular-subarray

# solution #
class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		currMin = currMax = 0
		minSum = maxSum = nums[0]
		
		totalSum = 0
		
		for num in nums:
			totalSum += num
			
			currMin = min(num, currMin + num)
			currMax = max(num, currMax + num)
			
			minSum = min(minSum, currMin)
			maxSum = max(maxSum, currMax)
		
		# max sum is either a subsequence or it spans either ends of the array
		return max(maxSum, totalSum - minSum) if maxSum > 0 else maxSum

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""