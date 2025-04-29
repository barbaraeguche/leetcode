# name: 1784. check if binary string has at most one segment of ones
# link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones

# solution #
class Solution:
	def checkOnesSegment(self, s: str) -> bool:
		string = ""
		
		for char in s:
			if char == "1":
				string += char
			else:
				string += " "
		
		return len(string.split()) == 1
	