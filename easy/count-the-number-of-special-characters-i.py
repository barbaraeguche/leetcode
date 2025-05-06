# name: 3120. count the number of special characters i
# link: https://leetcode.com/problems/count-the-number-of-special-characters-i

# solution #
class Solution:
	def numberOfSpecialChars(self, word: str) -> int:
		count = 0
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		
		# check if the upper and lower exist
		for alph in alphabets:
			if alph in word and alph.upper() in word:
				count += 1
		
		return count
	