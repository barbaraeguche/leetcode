# name: 2068. check whether two strings are almost equivalent
# link: https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent

# solution #
class Solution:
	def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		
		for char in alphabets:
			cnt1 = word1.count(char)
			cnt2 = word2.count(char)
			
			# if gone above the limit
			if abs(cnt1 - cnt2) > 3:
				return False
		
		return True
	