# name: 231. power of two
# link: https://leetcode.com/problems/power-of-two

# solution #
class Solution:
	def isPowerOfTwo(self, n: int) -> bool:
		if n <= 0:
			return False
		
		return bin(n)[2:].count('1') == 1