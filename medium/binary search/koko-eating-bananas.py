# name: 875. koko eating bananas
# link: https://leetcode.com/problems/koko-eating-bananas

# solution #
class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		# the upper boundary is the max of piles[i]
		l, r = 1, max(piles)
		# maximum possible value
		minK = r
		
		while l <= r:
			mid = (l + r) // 2
			
			# find rate at current k
			rate = self.calculateRate(piles, mid)
			
			if rate <= h:
				minK = mid
				r = mid - 1
			else:
				l = mid + 1
		
		return minK
	
	def calculateRate(self, piles: List[int], rate: int) -> int:
		time = 0
		
		for pile in piles:
			time += math.ceil(pile / rate)
		
		return time
