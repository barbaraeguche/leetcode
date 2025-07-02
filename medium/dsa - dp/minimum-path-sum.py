# name: 64. minimum path sum
# link: https://leetcode.com/problems/minimum-path-sum

# solution #
class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		
		pathSum = [[grid[0][0] for _ in range(cols)] for _ in range(rows)]
		
		# set the first row at each col
		for i in range(1, cols):
			pathSum[0][i] = pathSum[0][i-1] + grid[0][i]
		
		# set the first col at each row
		for i in range(1, rows):
			pathSum[i][0] = pathSum[i-1][0] + grid[i][0]
		
		for i in range(1, rows):
			for j in range(1, cols):
				# the min path sum is min(top, left) + current path num
				pathSum[i][j] = min(pathSum[i-1][j], pathSum[i][j-1]) + grid[i][j]
		
		# the min path sum is at the last row-col pair
		return pathSum[rows-1][cols-1]
	
"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""