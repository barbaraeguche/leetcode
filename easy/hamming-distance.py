# name: 461. hamming distance
# link: https://leetcode.com/problems/hamming-distance

# solution #
class Solution:
	def hammingDistance(self, x: int, y: int) -> int:
		count = 0
		
		bix, biy = bin(x)[2:], bin(y)[2:]
		
		while bix and biy:
			if bix[-1] != biy[-1]:
				count += 1
			
			bix = bix[:-1]
			biy = biy[:-1]
		
		count += (bix if bix else biy).count('1')
		
		return count