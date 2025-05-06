# name: 3498. reverse degree of a string
# link: https://leetcode.com/problems/reverse-degree-of-a-string

# solution #
class Solution:
	def reverseDegree(self, s: str) -> int:
		total, constant = 0, 26
		base = ord('a')
		
		for i, char in enumerate(s):
			prod = 26 - (ord(char) - base)
			total += (i + 1) * prod
		
		return total
