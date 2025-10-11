# name: 91. decode ways
# link: https://leetcode.com/problems/decode-ways

# solution #
class Solution:
	def numDecodings(self, s: str) -> int:
		def dfs(i, memo, n):
			# previously computed value
			if i in memo:
				return memo[i]
			
			# out of bound
			if i == n:
				return 1
			
			# impossible
			if s[i] == "0":
				return 0
			
			# end of string
			if i == n - 1:
				return 1
			
			ways = dfs(i + 1, memo, n)
			if s[i:i + 2] <= "26":
				ways += dfs(i + 2, memo, n)
			
			# store in memo
			memo[i] = ways
			return memo[i]
		
		return dfs(0, {}, len(s))

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""