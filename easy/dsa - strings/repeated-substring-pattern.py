# name: 459. repeated substring pattern
# link: https://leetcode.com/problems/repeated-substring-pattern

# solution #
class Solution:
	def repeatedSubstringPattern(self, s: str) -> bool:
		string, length = "", len(s)
		
		for char in s[:-1]:
			string += char
			
			# find if the substring is a factor of the original string
			q, r = divmod(length, len(string))
			
			# if the substring is a factor
			if r == 0:
				# if the string can be constructed
				if string * q == s:
					return True
		
		return False
