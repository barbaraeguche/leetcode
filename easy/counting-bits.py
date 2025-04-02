# name: 338. counting bits
# link: https://leetcode.com/problems/counting-bits

# solution #
class Solution:
	def countBits(self, n: int) -> List[int]:
		array = [0] * (n + 1)
		
		for i in range(1, n+1):
			array[i] = (bin(i)[2:]).count('1')
		
		return array