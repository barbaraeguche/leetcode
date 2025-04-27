# name: 1422. maximum score after splitting a string
# link: https://leetcode.com/problems/maximum-score-after-splitting-a-string

# solution #
class Solution:
	def maxScore(self, s: str) -> int:
		max_sum = -1
		
		for i, bit in enumerate(s[1:]):
			left = s[:i+1].count('0')
			right = s[i+1:].count('1')
			
			if (total := left + right) > max_sum:
				max_sum = total
		
		return max_sum
