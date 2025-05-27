# name: 200. number of islands
# link: https://leetcode.com/problems/number-of-islands

# solution #
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		rows, cols = len(grid), len(grid[0])
		
		# islands count
		islands = 0
		
		def bfs(r, c) -> None:
			# within range of grid
			if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
				grid[r][c] = "0"  # mark this as visited
				bfs(r-1, c)  # up
				bfs(r+1, c)  # down
				bfs(r, c-1)  # left
				bfs(r, c+1)  # right
		
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "1":  # island found
					bfs(r, c)
					islands += 1
		
		return islands
