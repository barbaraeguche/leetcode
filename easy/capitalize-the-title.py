# name: 2129. capitalize the title
# link: https://leetcode.com/problems/capitalize-the-title

# solution #
class Solution:
	def capitalizeTitle(self, title: str) -> str:
		formatted = ""
		
		for word in title.split():
			if len(word) < 3:
				formatted += f"{word.lower()} "
			else:
				formatted += f"{word[0].upper()}{word[1:].lower()} "
		
		return formatted.strip()