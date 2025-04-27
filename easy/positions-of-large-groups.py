# name: 830. positions of large groups
# link: https://leetcode.com/problems/positions-of-large-groups

# solution #
class Solution:
	def largeGroupPositions(self, s: str) -> List[List[int]]:
		sentences = self.group_char(s).split()
		idx, groups = 0, []
		
		for sen in sentences:
			n = len(sen)
			stop = idx + len(sen)
			
			# if it qualifies as a group
			if n >= 3:
				groups.append([idx, stop - 1])
			
			# increment index
			idx += len(sen)
		
		return groups
	
	@staticmethod
	def group_char(s: str) -> str:
		prefix = s[0]
		
		for i, char in enumerate(s[1:]):
			if prefix[-1] == char:
				prefix += char
			else:
				prefix += " " + char
		
		return prefix
	