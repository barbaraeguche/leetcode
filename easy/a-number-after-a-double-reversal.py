# name: 2119. a number after a double reversal
# link: https://leetcode.com/problems/a-number-after-a-double-reversal

# solution #
class Solution:
	def isSameAfterReversals(self, num: int) -> bool:
		rev_one = int(str(num)[::-1])
		return num == int(str(rev_one)[::-1])
	