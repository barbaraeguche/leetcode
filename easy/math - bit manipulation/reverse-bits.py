# name: 190. reverse bits
# link: https://leetcode.com/problems/reverse-bits

# solution #
class Solution:
	def reverseBits(self, n: int) -> int:
		string = ""
		
		for i in range(31, -1, -1):
			bit = (n >> i) & 1
			string = str(bit) + string
		
		return int(string, 2)
