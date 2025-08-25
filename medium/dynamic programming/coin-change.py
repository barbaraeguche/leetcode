# name: 322. coin change
# link: https://leetcode.com/problems/coin-change

# solution #
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		m = amount
		
		dp = [m + 1] * (m + 1)
		dp[0] = 0  # you can get 0 using nothing
		
		for a in range(1, m + 1):
			for c in coins:
				if a >= c:
					dp[a] = min(dp[a], 1 + dp[a-c])
		
		return -1 if dp[m] == m + 1 else dp[m]
	
"""
time complexity:
- O(n * m); n is the length of coins, m is the amount

space complexity:
- O(m)
"""