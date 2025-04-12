# name: 917. reverse only letters
# link: https://leetcode.com/problems/reverse-only-letters

# solution #
class Solution:
	def reverseOnlyLetters(self, s: str) -> str:
		string = [''] * len(s)
		l, r = 0, len(s) - 1
		
		while l <= r:
			while l < r and not self.is_letter(s[l]):
				string[l] = s[l]
				l += 1
			
			while r > l and not self.is_letter(s[r]):
				string[r] = s[r]
				r -= 1
			
			string[l], string[r] = s[r], s[l]
			l += 1
			r -= 1
		
		return ''.join(string)
	
	@staticmethod
	def is_letter(char: str):
		return char.isalpha()