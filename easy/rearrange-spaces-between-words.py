# name: 1592. rearrange spaces between words
# link: https://leetcode.com/problems/rearrange-spaces-between-words

# solution #
class Solution:
	def reorderSpaces(self, text: str) -> str:
		splitted = text.split()
		
		# count total spaces
		count = sum(1 for char in text if char == " ")
		
		# length of wordings, q, and r
		length = len(splitted) - 1
		
		# if only one word
		if length == 0:
			return f"{splitted[0]}{(' ' * count)}"
		
		q, r = divmod(count, length)
		
		return f"{(' ' * q).join(splitted)}{(' ' * r)}"
