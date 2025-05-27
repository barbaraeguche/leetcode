# name: 48. rotate image
# link: https://leetcode.com/problems/rotate-image

# solution #
class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# n x n matrix
		length = len(matrix)
		seen = set()
		
		for i in range(length):
			for j in range(length):
				if (i, j) not in seen:
					# swap numbers
					matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
					# add (j, i) to set to prevent re-swap
					seen.add((j, i))
			
			# reverse the current row
			matrix[i] = matrix[i][::-1]
