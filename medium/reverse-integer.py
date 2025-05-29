# name: 7. reverse integer
# link: https://leetcode.com/problems/reverse-integer

# solution #
class Solution:
	class Solution:
		def reverse(self, x: int) -> int:
			MIN, MAX = -2 ** 31, (2 ** 31) - 1
			
			positive = abs(x)
			num = int(str(positive)[::-1])
			
			# out of range
			if not MIN <= num <= MAX:
				return 0
			
			return num if positive == x else -num
