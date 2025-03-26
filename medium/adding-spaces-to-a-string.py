# name: 2109. adding spaces to a string
# link: https://leetcode.com/problems/adding-spaces-to-a-string

# solution #
class Solution:
	def addSpaces(self, s: str, spaces: List[int]) -> str:
		formatted = ""
		
		for i, num in enumerate(spaces):
			if i == 0:
				formatted += f"{s[:num]} "
			else:
				formatted += f"{s[spaces[i - 1]:num]} "
			
			if i == len(spaces) - 1:
				formatted += f"{s[num:]}"
		
		return formatted