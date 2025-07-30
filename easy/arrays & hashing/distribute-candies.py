# name: 575. distribute candies
# link: https://leetcode.com/problems/distribute-candies

# solution #
class Solution:
	def distributeCandies(self, candyType: List[int]) -> int:
		count = Counter(candyType)
		
		maxCanEat = len(candyType) // 2
		diffTypes = len(count.keys())
		
		return min(diffTypes, maxCanEat)
