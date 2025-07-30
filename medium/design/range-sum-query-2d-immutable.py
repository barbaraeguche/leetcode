# name: 304. range sum query 2d immutable
# link: https://leetcode.com/problems/range-sum-query-2d-immutable

# solution #
class NumMatrix:
	
	def __init__(self, matrix: List[List[int]]):
		rows, cols = len(matrix), len(matrix[0])
		self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
		
		for r in range(rows):
			# set the first col
			self.matrix[r][0] = matrix[r][0]
			
			# set the remaining cols
			for c in range(1, cols):
				self.matrix[r][c] = self.matrix[r][c-1] + matrix[r][c]
	
	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		regionSum = 0
		
		for r in range(row1, row2 + 1):
			rightSum = self.matrix[r][col2]
			leftSum = self.matrix[r][col1 - 1]if col1 > 0 else 0
			
			# add up the sum for each row
			regionSum += rightSum - leftSum
		
		return regionSum

"""
time complexity:
- O(n); n is the number of rows

space complexity:
- O(n * m); m is the number of cols
"""