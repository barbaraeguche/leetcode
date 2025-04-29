# name: 2309. greatest english letter in upper and lower case
# link: https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case

# solution #
class Solution:
	def greatestLetter(self, s: str) -> str:
		array = []
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		
		# check if the upper and lower exist
		for alph in alphabets:
			if alph in s and alph.upper() in s:
				array.append(alph)
		
		# sort the array
		array.sort()
		
		return "" if len(array) == 0 else array[-1].upper()
	