# name: 2496. maximum value of a string in an array
# link: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array

# solution #
class Solution:
	def maximumValue(self, strs: List[str]) -> int:
		count = 0
		
		for word in strs:
			try:
				count = max(count, int(word))
			except ValueError:
				count = max(count, len(word))
		
		return count
