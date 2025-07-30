# name: 63. unique paths ii
# link: https://leetcode.com/problems/unique-paths-ii

# solution #
class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		rows, cols = len(obstacleGrid), len(obstacleGrid[0])
		
		def uniquePaths(r, c, memo):
			key = f"{r}:{c}"
			
			# been here before
			if key in memo:
				return memo[key]
			
			# bottom right reached
			if (r, c) == (rows - 1, cols - 1):
				return 1 if obstacleGrid[r][c] == 0 else 0
			
			# out of bounds
			if not (
				0 <= r < rows and
				0 <= c < cols and
				obstacleGrid[r][c] == 0
			):
				return 0
			
			# cache the current unique paths
			memo[key] = uniquePaths(r+1, c, memo) + uniquePaths(r, c+1, memo)
			return memo[key]
		
		return uniquePaths(0, 0, {})
	
"""
time complexity:
- O(n * m); n is the number of rows, m is the number of cols

space complexity:
- O(n * m)
"""