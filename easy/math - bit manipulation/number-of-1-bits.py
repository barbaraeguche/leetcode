# name: 191. number of 1 bits
# link: https://leetcode.com/problems/number-of-1-bits

# solution #
class Solution:
	def hammingWeight(self, n: int) -> int:
		count = 0
	
		for i in range(31, -1, -1):
			bit = (n >> i) & 1
			count += bit
		
		return count

"""
time complexity:
- O(1)

space complexity:
- O(1)
"""