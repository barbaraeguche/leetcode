# name: 338. counting bits
# link: https://leetcode.com/problems/counting-bits

# solution #
class Solution:
	def countBits(self, n: int) -> List[int]:
		dp = [0] * (n + 1)
		
		for i in range(n + 1):
			dp[i] = dp[i >> 1] + (i & 1)
			
		return dp
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""