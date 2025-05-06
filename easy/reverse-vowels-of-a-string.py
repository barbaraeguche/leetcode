# name: 345. reverse vowels of a string
# link: https://leetcode.com/problems/reverse-vowels-of-a-string

# solution #
class Solution:
	def reverseVowels(self, s: str) -> str:
		if len(s) == 1: return s
		
		array = [""] * len(s)
		l, r = 0, len(s) - 1
		
		while l <= r:
			while l < r and not self.is_vowel(s[l]):
				array[l] = s[l]
				l += 1
			
			while r > l and not self.is_vowel(s[r]):
				array[r] = s[r]
				r -= 1
			
			array[l], array[r] = s[r], s[l]
			l += 1
			r -= 1
		
		return ''.join(array)
	
	@staticmethod
	def is_vowel(char: str):
		return char.lower() in ['a', 'e', 'i', 'o', 'u']
	