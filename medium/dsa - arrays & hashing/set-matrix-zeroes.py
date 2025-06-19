# name: 73. set matrix zeroes
# link: https://leetcode.com/problems/set-matrix-zeroes

# solution #
class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		rows, cols = len(matrix), len(matrix[0])
		
		hasZeroRow = any(matrix[0][c] == 0 for c in range(cols))
		hasZeroCol = any(matrix[r][0] == 0 for r in range(rows))
		
		# step 1: mark first row and column
		for r in range(1, rows):
			for c in range(1, cols):
				if matrix[r][c] == 0:
					matrix[r][0] = 0
					matrix[0][c] = 0
		
		# step 2: apply the marks
		for r in range(1, rows):
			for c in range(1, cols):
				if matrix[r][0] == 0 or matrix[0][c] == 0:
					matrix[r][c] = 0
		
		# step 3: zero first row if needed
		if hasZeroRow:
			for c in range(cols):
				matrix[0][c] = 0
		
		# step 4: zero first col if needed
		if hasZeroCol:
			for r in range(rows):
				matrix[r][0] = 0

"""
time complexity:
- O(n * m)

space complexity:
- O(1)
"""