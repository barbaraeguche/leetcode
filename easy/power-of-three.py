# name: 326. power of three
# link: https://leetcode.com/problems/power-of-three

# solution #
class Solution:
	def isPowerOfThree(self, n: int) -> bool:
		return n > 0 and 1162261467 % n == 0
	