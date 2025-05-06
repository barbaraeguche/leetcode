# name: 1446. consecutive characters
# link: https://leetcode.com/problems/consecutive-characters

# solution #
class Solution:
	def maxPower(self, s: str) -> int:
		chunks = self.group_char(s)
		max_len = -1
		
		for chunk in chunks.split():
			max_len = max(len(chunk), max_len)
		
		return max_len
	
	@staticmethod
	def group_char(s: str) -> str:
		prefix = s[0]
		
		for char in s[1:]:
			if char == prefix[-1]:
				prefix += char
			else:
				prefix += " " + char
		
		return prefix
	