# name: 7. reverse integer
# link: https://leetcode.com/problems/reverse-integer

# solution #
class Solution:
	def reverse(self, x: int) -> int:
		rev_x = str(-1 * x if x < 0 else x)[::-1]
		min_int, max_int = -2147483648, 2147483647
		
		if not min_int <= int(rev_x) <= max_int:
			return 0
		
		return -1 * int(rev_x) if x < 0 else int(rev_x)