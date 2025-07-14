# name: 994. rotting oranges
# link: https://leetcode.com/problems/rotting-oranges

# solution #
class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		
		minutes, queue = 0, deque()
		
		# add all rotten oranges to the queue
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == 2:
					queue.append((r, c))
		
		# rot all other oranges
		while queue:
			length = len(queue)
			
			for _ in range(length):
				nr, nc = queue.popleft()
				
				for dr, dc in directions:
					row, col = dr + nr, dc + nc
					
					# within the grid range
					if (
						0 <= row < rows and
						0 <= col < cols and
						grid[row][col] == 1
					):
						grid[row][col] = 2
						queue.append((row, col))
			
			# increment for current batch of rotten oranges
			minutes += 1 if queue else 0
		
		# check if any orange could not rot
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == 1:
					return -1
		
		return minutes

"""
time complexity:
- O(n * m)

space complexity:
- O(n)
"""