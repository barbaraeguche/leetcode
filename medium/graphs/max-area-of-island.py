# name: 695. max area of island
# link: https://leetcode.com/problems/max-area-of-island

# solution #
class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		
		# area count
		area = 0
		
		def dfs(r, c) -> int:
			# not within range of grid
			if not (
				0 <= r < rows and
				0 <= c < cols and
				grid[r][c] == 1
			):
				return 0
			
			grid[r][c] = 0
			return (
				1 +
				dfs(r-1, c) + dfs(r+1, c) +
				dfs(r, c-1) + dfs(r, c+1)
			)  # up, down, left, right
		
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == 1:
					area = max(area, dfs(r, c))
		
		return area

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""