# name: 733. flood fill
# link: https://leetcode.com/problems/flood-fill

# solution #
class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
		rows, cols = len(image), len(image[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		
		seen, queue = set(), deque([(sr, sc)])
		
		# keep track of initial start pixel
		sameColor = image[sr][sc]
		
		while queue:
			for _ in range(len(queue)):
				nr, nc = queue.popleft()
				
				# color the image
				image[nr][nc] = color
				
				# mark path as seen
				seen.add((nr, nc))
				
				for dr, dc in directions:
					row, col = nr + dr, nc + dc
					
					# must be within bounds
					if (
						0 <= row < rows and
						0 <= col < cols and
						(row, col) not in seen and
						image[row][col] == sameColor
					):
						queue.append((row, col))
		
		return image

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""