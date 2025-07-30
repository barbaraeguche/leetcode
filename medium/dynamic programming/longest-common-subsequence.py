# name: 1143. longest common subsequence
# link: https://leetcode.com/problems/longest-common-subsequence

# solution #
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		rows, cols = len(text1), len(text2)
		
		def commonSeq(r, c, memo):
			# out of bounds
			if r == rows or c == cols:
				return 0
			
			key = f"{r}:{c}"
			
			# been here before
			if key in memo:
				return memo[key]
			
			# found a sequence, move r+1, c+1
			if text1[r] == text2[c]:
				memo[key] = commonSeq(r+1, c+1, memo) + 1
			# explore either possible sequence
			else:
				memo[key] = max(commonSeq(r+1, c, memo), commonSeq(r, c+1, memo))
			
			return memo[key]
		
		return commonSeq(0, 0, {})

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""