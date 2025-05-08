# name: 74. search a 2d matrix
# link: https://leetcode.com/problems/search-a-2d-matrix

# solution #
class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		l, r = 0, len(matrix) - 1
		
		while l <= r:
			a, b = matrix[l], matrix[r]
			
			if target in a or target in b:
				return True
			
			l += 1
			r -= 1
		
		return False
