# name: 1071. greatest common divisor of strings
# link: https://leetcode.com/problems/greatest-common-divisor-of-strings

# solution #
class Solution:
	def gcdOfStrings(self, str1: str, str2: str) -> str:
		len1, len2 = len(str1), len(str2)
		
		string = longest = ""
		
		for char in str2:
			string += char
			lenS = len(string)
			
			# check if prefix is a factor
			q1, r1 = divmod(len1, lenS)
			q2, r2 = divmod(len2, lenS)
			
			# prefix is a factor of both str1 and str2
			if (r1, r2) == (0, 0):
				if (string * q1, string * q2) == (str1, str2):
					longest = max(longest, string, key=len)
		
		return longest
