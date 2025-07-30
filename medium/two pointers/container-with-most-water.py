# name: 11. container with most water
# link: https://leetcode.com/problems/container-with-most-water

# solution #
class Solution:
	def maxArea(self, heights: List[int]) -> int:
		l, r = 0, len(heights) - 1
		
		water = 0
		
		while l < r:
			a, b = heights[l], heights[r]
			
			# get the min between the two heights
			minimum = min(a, b)
			# multiply by the number of spaces between them
			holdings = minimum * (r-l)
			
			# keep track of max water
			water = max(water, holdings)
			
			# reduce or increase by min
			if a < b:
				l += 1
			else:
				r -= 1
		
		return water

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""