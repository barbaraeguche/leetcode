# name: 3146. permutation difference between two strings
# link: https://leetcode.com/problems/permutation-difference-between-two-strings

# solution #
class Solution:
	def findPermutationDifference(self, s: str, t: str) -> int:
		# keep track
		count = 0
		
		for char in s:
			i = s.index(char)
			j = t.index(char)
			
			count += abs(i - j)
		
		return count
