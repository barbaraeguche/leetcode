# name: 476. number complement
# link: https://leetcode.com/problems/number-complement

# solution #
class Solution:
	def findComplement(self, num: int) -> int:
		complement = ""
		
		for bit in bin(num)[2:]:
			if bit == "0":
				complement += "1"
			else:
				complement += "0"
		
		return int(complement, 2)