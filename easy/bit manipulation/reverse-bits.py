# name: 190. reverse bits
# link: https://leetcode.com/problems/reverse-bits

# solution #
class Solution:
	def reverseBits(self, n: int) -> int:
		number = 0
		
		for i in range(32):
			bit = (n >> i) & 1
			number += bit << (31 - i)
		
		return number

"""
time complexity:
- O(1)

space complexity:
- O(1)
"""