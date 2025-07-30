# name: 1091. shortest path in binary matrix
# link: https://leetcode.com/problems/shortest-path-in-binary-matrix

# solution #
class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		# edge case: grid[0][0] == 1
		if grid[0][0] == 1:
			return -1
		
		# n x n grid
		size = len(grid)
		directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
		
		path, queue = 1, deque([(0, 0)])
		
		while queue:
			length = len(queue)
			
			for _ in range(length):
				nr, nc = queue.popleft()
				
				# bottom right reached
				if nr == size - 1 and nc == size - 1:
					return path
				
				for dr, dc in directions:
					row, col = nr + dr, nc + dc
					
					# within the grid range
					if (
						0 <= row < size and
						0 <= col < size and
						grid[row][col] == 0
					):
						grid[row][col] = 1
						queue.append((row, col))
			
			# increment for current batch of paths
			path += 1
		
		return -1

"""
time complexity:
- O(n^2)

space complexity:
- O(n^2)
"""