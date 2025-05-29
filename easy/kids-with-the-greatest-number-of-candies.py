# name: 1431. kids with the greatest number of candies
# link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

# solution #
class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		max_candy = max(candies)
		
		for i, candy in enumerate(candies):
			candies[i] = True if candy + extraCandies >= max_candy else False
			
		return candies
	