# name: 67. add binary
# link: https://leetcode.com/problems/add-binary

# solution #
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		return bin(int(a, 2) + int(b, 2))[2:]
	