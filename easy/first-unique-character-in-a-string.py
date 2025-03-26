# name: 387. first unique character in a string
# link: https://leetcode.com/problems/first-unique-character-in-a-string

# solution #
class Solution:
	def firstUniqChar(self, s: str) -> int:
		min_idx = 100001
		filtered = [char for char in set(s) if s.count(char) == 1]
		
		for f in filtered:
			min_idx = min(min_idx, s.index(f))
		
		return -1 if min_idx == 100001 else min_idx