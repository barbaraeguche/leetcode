# name: 1961. check if string is a prefix of array
# link: https://leetcode.com/problems/check-if-string-is-a-prefix-of-array

# solution #
class Solution:
	def isPrefixString(self, s: str, words: List[str]) -> bool:
		string = ""
		
		for word in words:
			string += word
			
			if string == s:
				return True
		
		return False
	