# name: 1796. second largest digit in a string
# link: https://leetcode.com/problems/second-largest-digit-in-a-string

# solution #
class Solution:
	def secondHighest(self, s: str) -> int:
		filtered = list(set(filter(str.isdigit, s)))
		found = sorted(filtered, reverse=True)
		
		return -1 if len(found) < 2 else int(found[1])