# name: 1903. largest odd number in string
# link: https://leetcode.com/problems/largest-odd-number-in-string

# solution #
class Solution:
	def largestOddNumber(self, num: str) -> str:
		while num:
			# if the last char is odd, return
			if int(num[-1]) % 2 == 1:
				return num
			
			num = num[:-1]
		
		return ""
	