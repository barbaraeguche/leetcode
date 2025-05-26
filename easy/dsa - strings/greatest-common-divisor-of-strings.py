# name: 1071. greatest common divisor of strings
# link: https://leetcode.com/problems/greatest-common-divisor-of-strings

# solution #
class Solution:
	def gcdOfStrings(self, str1: str, str2: str) -> str:
		length_str1 = len(str1)
		length_str2 = len(str2)
		
		prefix = longest = ""
		
		for char in str2:
			prefix += char
			length_prefix = len(prefix)
			
			# check if prefix is a factor
			qstr1, rstr1 = divmod(length_str1, length_prefix)
			qstr2, rstr2 = divmod(length_str2, length_prefix)
			
			# prefix is a factor of both str1 and str2
			if (rstr1, rstr2) == (0, 0):
				# if prefix can be constructed
				if (prefix * qstr1, prefix * qstr2) == (str1, str2):
					longest = max(longest, prefix, key=len)
		
		return longest
