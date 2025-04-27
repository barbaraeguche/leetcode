# name: 1844. replace all digits with characters
# link: https://leetcode.com/problems/replace-all-digits-with-characters

# solution #
class Solution:
	def replaceDigits(self, s: str) -> str:
		for i, char in enumerate(s):
			if i % 2 != 0:
				prev = s[i-1]
				s = f"{s[:i]}{chr(ord(prev) + int(s[i]))}{s[i+1:]}"
		
		return s
	