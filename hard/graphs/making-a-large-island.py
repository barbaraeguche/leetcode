# name: 827. making-a-large-island
# link: https://leetcode.com/problems/making-a-large-island

# solution #
class Solution:
	def largestIsland(self, grid: List[List[int]]) -> int:
		n, directions = len(grid), [[-1, 0], [1, 0], [0, -1], [0, 1]]
		islandId, areaMap = 2, defaultdict(int)
		
		def dfs(r, c):
			# not within range of grid
			if not (
				0 <= r < n and
				0 <= c < n and
				grid[r][c] == 1
			):
				return 0
			
			grid[r][c] = islandId
			return (
				1 +
				dfs(r-1, c) + dfs(r+1, c) +
				dfs(r, c-1) + dfs(r, c+1)
			)  # up, down, left, right
		
		# take note of the initial island areas
		for r in range(n):
			for c in range(n):
				if grid[r][c] == 1:
					# give each island a unique id
					areaMap[islandId] = dfs(r, c)
					islandId += 1
		
		# largest maximum
		maxArea = 0
		
		for r in range(n):
			for c in range(n):
				# change at most one 0 to 1
				if grid[r][c] == 0:
					currArea, surrounding = 1, set()
					
					for dr, dc in directions:
						row, col = r + dr, c + dc
						
						# within range of grid
						if (
							0 <= row < n and
							0 <= col < n and
							grid[row][col] != 0
						):
							surrounding.add(grid[row][col])
					
					# make a large island
					for iD in surrounding:
						currArea += areaMap[iD]
					
					maxArea = max(maxArea, currArea)
		
		return maxArea if maxArea else n ** 2

"""
time complexity:
- O(n^2)

space complexity:
- O(n^2)
"""