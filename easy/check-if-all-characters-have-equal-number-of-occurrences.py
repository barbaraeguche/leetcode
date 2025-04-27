# name: 1941. check if all characters have equal number of occurrences
# link: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences

# solution #
class Solution:
	def areOccurrencesEqual(self, s: str) -> bool:
		reference = s.count(s[0])
		
		for char in set(s):
			if reference != s.count(char):
				return False
		
		return True
	