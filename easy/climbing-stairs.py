# name: 70. climbing stairs
# link: https://leetcode.com/problems/climbing-stairs

# solution #
class Solution:
	def climbStairs(self, n: int) -> int:
		memo = { 1:1, 2:2 }
		
		def climb(n: int) -> int:
			if n in memo:
				return memo[n]
			
			memo[n] = climb(n - 1) + climb(n - 2)
			return memo[n]
		
		return climb(n)
	