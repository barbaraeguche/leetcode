# name: 1762. buildings with an ocean view
# link: https://leetcode.com/problems/buildings-with-an-ocean-view

# solution #
class Solution:
	def findBuildings(self, heights: List[int]) -> List[int]:
		length = len(heights)
		
		# to store the suffix maximum
		suffixMax = [0] * length
		
		for i in range(1, length):
			suffixMax[-i-1] = max(suffixMax[-i], heights[-i])
		
		indices = []
		
		for i, num in enumerate(heights):
			if num > suffixMax[i]:
				indices.append(i)
		
		return indices
	