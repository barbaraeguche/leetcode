# name: 191. number of 1 bits
# link: https://leetcode.com/problems/number-of-1-bits

# solution #
class Solution:
	def hammingWeight(self, n: int) -> int:
		return bin(n)[2:].count('1')