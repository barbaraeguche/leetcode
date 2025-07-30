# name: 463. island perimeter
# link: https://leetcode.com/problems/island-perimeter

# solution #
class Solution:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		
		perimeter, seen = 0, set()
		
		def dfs(r, c):
			# out of range, water; a valid perimeter
			if not (
				0 <= r < rows and
				0 <= c < cols and
				grid[r][c] == 1
			):
				return 1
			
			# previously visited
			if (r, c) in seen:
				return 0
			
			seen.add((r, c))
			return (
				dfs(r-1, c) +
				dfs(r+1, c) +
				dfs(r, c-1) +
				dfs(r, c+1)
			)
		
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == 1:
					perimeter += dfs(r, c)
		
		return perimeter
	
"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""