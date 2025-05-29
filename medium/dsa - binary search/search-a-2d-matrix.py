# name: 74. search a 2d matrix
# link: https://leetcode.com/problems/search-a-2d-matrix

# solution #
class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		l, r = 0, len(matrix) - 1
		
		while l <= r:
			if target in matrix[l] or target in matrix[r]:
				return True
			
			l, r = l + 1, r - 1
		
		return False
