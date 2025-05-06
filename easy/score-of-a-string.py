# name: 3110. score of a string
# link: https://leetcode.com/problems/score-of-a-string

# solution #
class Solution:
	def scoreOfString(self, s: str) -> int:
		count = 0
		
		for i in range(len(s) - 1):
			# get the ascii value
			a, b = ord(s[i]), ord(s[i+1])
			# calculate sum
			count += abs(a - b)
		
		return count
