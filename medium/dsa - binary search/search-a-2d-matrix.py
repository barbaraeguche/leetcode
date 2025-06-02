# name: 74. search a 2d matrix
# link: https://leetcode.com/problems/search-a-2d-matrix

# solution #
class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		rows, cols = len(matrix), len(matrix[0])
		l, r = 0, rows * cols - 1
		
		while l <= r:
			mid = (l + r) // 2
			# find the (row, col) of middle value
			row, col = mid // cols, mid % cols
			# get the value
			num = matrix[row][col]
			
			if num == target:
				return True
			
			if num > target:
				r = mid - 1
			else:
				l = mid + 1
		
		return False
