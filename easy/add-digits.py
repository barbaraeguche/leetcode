# name: 258. add digits
# link: https://leetcode.com/problems/add-digits

# solution #
class Solution:
	def addDigits(self, num: int) -> int:
		if num < 10:
			return num
		
		if num % 9 == 0: return 9
		
		return num % 9
	