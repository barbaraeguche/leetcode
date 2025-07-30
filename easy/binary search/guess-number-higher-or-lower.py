# name: 374. guess number higher or lower
# link: https://leetcode.com/problems/guess-number-higher-or-lower

# solution #
class Solution:
	def guessNumber(self, n: int) -> int:
		l, r = 1, n
		
		while l <= r:
			mid = (l + r) // 2
			num = guess(mid)
			
			if num > 0:
				l = mid + 1
			elif num < 0:
				r = mid - 1
			else:
				return mid
		
		return -1
	