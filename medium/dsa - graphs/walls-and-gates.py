# name: 286. walls and gates
# link: https://leetcode.com/problems/walls-and-gates

# solution #
class Solution:
	def wallsAndGates(self, rooms: List[List[int]]) -> None:
		"""
		Do not return anything, modify rooms in-place instead.
		"""
		rows, cols = len(rooms), len(rooms[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		
		INF, queue = 2147483647, deque()
		
		for i in range(rows):
			for j in range(cols):
				# add all the gates to the queue
				if rooms[i][j] == 0:
					queue.append((i, j))
		
		distance = 1
		
		while queue:
			length = len(queue)
			
			for _ in range(length):
				nr, nc = queue.popleft()
				
				for dr, dc in directions:
					row, col = nr + dr, nc + dc
					
					# within bounds
					if (
						0 <= row < rows and
						0 <= col < cols and
						rooms[row][col] == INF
					):
						# mark as a visited
						rooms[row][col] = distance
						queue.append((row, col))
			
			distance += 1

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""