# name: 2828. check if a string is an acronym of words
# link: https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words

# solution #
class Solution:
	def isAcronym(self, words: List[str], s: str) -> bool:
		string = ""
		
		for word in words:
			string += word[0]
		
		return string == s
