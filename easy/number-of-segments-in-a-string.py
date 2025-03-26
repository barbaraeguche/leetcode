# name: 434. number of segments in a string
# link: https://leetcode.com/problems/number-of-segments-in-a-string

# solution #
class Solution:
	def countSegments(self, s: str) -> int:
		return len(s.split())