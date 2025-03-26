# name: 2264. largest 3 same digit number in string
# link: https://leetcode.com/problems/largest-3-same-digit-number-in-string

# solution #
class Solution:
	def largestGoodInteger(self, num: str) -> str:
		max_three = "-1"
		
		for i in range(10):
			if (n := str(i) * 3) in num and n > max_three:
				max_three = n
		
		return "" if max_three == "-1" else max_three