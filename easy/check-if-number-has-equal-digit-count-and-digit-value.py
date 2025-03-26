# name: 2283. check if number has equal digit count and digit value
# link: https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

# solution #
class Solution:
	def digitCount(self, num: str) -> bool:
		for i, n in enumerate(num):
			if num.count(str(i)) != int(n):
				return False
		
		return True