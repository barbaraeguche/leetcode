# name: 1137. n-th tribonacci number
# link: https://leetcode.com/problems/n-th-tribonacci-number

# solution #
class Solution:
	def tribonacci(self, n: int) -> int:
		dp = [0] * 38
		dp[0], dp[1], dp[2] = 0, 1, 1
		
		for i in range(3, n + 1):
			dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
		
		return dp[n]
	