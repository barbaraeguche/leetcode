# name: 2379. minimum recolors to get k consecutive black blocks
# link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

# solution #
class Solution:
	def minimumRecolors(self, blocks: str, k: int) -> int:
		currMin = minCount = 0
		
		for i in range(k):
			if blocks[i] == "W":
				currMin += 1
		
		# base current min
		minCount = currMin
		
		for i in range(k, len(blocks)):
			# removing from the window
			if blocks[i - k] == "W":
				currMin -= 1
			
			# adding to the window
			if blocks[i] == "W":
				currMin += 1
			
			# current min operations
			minCount = min(minCount, currMin)
		
		return minCount

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""