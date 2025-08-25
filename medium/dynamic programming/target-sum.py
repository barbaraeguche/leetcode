# name: 494. target sum
# link: https://leetcode.com/problems/target-sum

# solution #
class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		dp = defaultdict(int)
		dp[0] = 1
		
		for i in range(len(nums)):
			dpCopy = defaultdict(int)  # a copy of the current dp
			
			for key, count in dp.items():
				dpCopy[key - nums[i]] += count
				dpCopy[key + nums[i]] += count
			
			# update the table
			dp = dpCopy
		
		return dp[target]
	
"""
time complexity:
- O()

space complexity:
- O()
"""