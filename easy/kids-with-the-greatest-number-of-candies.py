# name: 1431. kids with the greatest number of candies
# link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

# solution #
class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		max_candies = max(candies)
		array = []
		
		for candy in candies:
			array.append(True if candy + extraCandies >= max_candies else False)
		
		return array
	