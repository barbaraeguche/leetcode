# name: 14. longest common prefix
# link: https://leetcode.com/problems/longest-common-prefix

# solution #
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if len(strs) == 1:
			return strs[0]
		
		# initialize the first word
		base = strs[0]
		
		for word in strs[1:]:
			while not word.startswith(base):
				base = base[:-1]
		
		return base