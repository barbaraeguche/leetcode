# name: 1143. longest common subsequence
# link: https://leetcode.com/problems/longest-common-subsequence

# solution #
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		n, m = len(text1), len(text2)
		dp = [0] * (m + 1)
		
		for i in range(n - 1, -1, -1):
			dpCopy = [0] * (m + 1)
			
			for j in range(m - 1, -1, -1):
				if text1[i] == text2[j]:
					dpCopy[j] = 1 + dp[j+1]
				else:
					dpCopy[j] = max(dp[j], dpCopy[j+1])
			
			dp = dpCopy
		
		return dp[0]

"""
time complexity:
- O(n * m)

space complexity:
- O(m)
"""