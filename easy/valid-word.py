# name: 3136. valid word
# link: https://leetcode.com/problems/valid-word

# solution #
class Solution:
	def isValid(self, word: str) -> bool:
		vow = cons = 0
		
		# length check
		if len(word) < 3:
			return False
		
		# alphanumerical check
		for w in word:
			if not w.isalnum():
				return False
		
		# vowel + consonant check
		for w in word.lower():
			if w in "aeiou":
				vow += 1
			if w in "bcdfghjklmnpqrstvwxyz":
				cons += 1
		
		return vow >= 1 and cons >= 1
