# name: 2710. remove trailing zeros from a string
# link: https://leetcode.com/problems/remove-trailing-zeros-from-a-string

# solution #
class Solution:
	def removeTrailingZeros(self, num: str) -> str:
		while num[-1] == "0":
			num = num[:-1]
		
		return num
	