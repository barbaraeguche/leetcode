# name: 2351. first letter to appear twice
# link: https://leetcode.com/problems/first-letter-to-appear-twice

# solution #
class Solution:
	def repeatedCharacter(self, s: str) -> str:
		seen = set()
		
		for char in s:
			if char in seen:
				return char
			
			seen.add(char)
		
		return ""