# name: 416. partition equal subset sum
# link: https://leetcode.com/problems/partition-equal-subset-sum

# solution #
class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		total = sum(nums)
		
		# impossible to split
		if total % 2 == 1:
			return False
		
		n, m = len(nums), total // 2
		dp = [0] * (m + 1)
		
		# handle edge cases
		for i in range(m + 1):
			if i >= nums[0]:
				dp[i] = nums[0]
		
		for i in range(1, n):
			dpCopy = dp[:]  # a copy of the current dp
			
			for j in range(1, m + 1):
				skip = dpCopy[j]  # not take this profit
				
				include = 0
				# if the current capacity can carry the i-th
				# weight, how much profit can we make?
				if j >= nums[i]:
					include = nums[i] + dp[j - nums[i]]
				
				# keep track of the current max profit
				dpCopy[j] = max(include, skip)
			
			# update the table
			dp = dpCopy
		
		return dp[m] == m

"""
time complexity:
- O(n * m)

space complexity:
- O(m)
"""