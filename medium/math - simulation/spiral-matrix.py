# name: 54. spiral matrix
# link: https://leetcode.com/problems/spiral-matrix

# solution #
class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		left, right = 0, len(matrix[0])
		top, bottom = 0, len(matrix)
		
		result = []
		
		while top < bottom and left < right:
			# get all top row elements
			for i in range(left, right):
				result.append(matrix[top][i])
			top += 1
			
			# get all right column elements
			for i in range(top, bottom):
				result.append(matrix[i][right - 1])
			right -= 1
			
			# to not process an already processed row or column
			if not (top < bottom and left < right):
				break
			
			# get all bottom row elements
			for i in range(right - 1, left - 1, -1):
				result.append(matrix[bottom - 1][i])
			bottom -= 1
			
			# get all left column elements
			for i in range(bottom - 1, top - 1, -1):
				result.append(matrix[i][left])
			left += 1
		
		return result
