# name: 3019. number of changing keys
# link: https://leetcode.com/problems/number-of-changing-keys

# solution #
class Solution:
	def countKeyChanges(self, s: str) -> int:
		s, count = s.lower(), 0
		
		for i in range(len(s) - 1):
			count += 1 if s[i] != s[i+1] else 0
		
		return count
