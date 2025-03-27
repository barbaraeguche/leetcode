# name: 2413. smallest even multiple
# link: https://leetcode.com/problems/smallest-even-multiple

# solution #
class Solution:
	def smallestEvenMultiple(self, n: int) -> int:
		return n if n % 2 == 0 else n * 2