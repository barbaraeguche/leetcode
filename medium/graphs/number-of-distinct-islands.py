# name: 694. number of distinct islands
# link: https://leetcode.com/problems/number-of-distinct-islands

# solution #
class Solution:
	def numDistinctIslands(self, grid: List[List[int]]) -> int:
		n, m = len(grid), len(grid[0])
		
		def dfs(i, j, direction):
			# within the grid
			if not (
				0 <= i < n and
				0 <= j < m and
				grid[i][j] == 1
			):
				return
			
			# mark this as visited
			grid[i][j] = 0
			
			# track the current direction
			path.append(direction)
			
			dfs(i - 1, j, "U")  # up
			dfs(i + 1, j, "D")  # down
			dfs(i, j - 1, "L")  # left
			dfs(i, j + 1, "R")  # right
			
			path.append("B")
		
		uniqueIslands = set()
		
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 1:
					path = []
					dfs(i, j, "")
					
					if path:
						uniqueIslands.add("".join(path))
		
		return len(uniqueIslands)

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""