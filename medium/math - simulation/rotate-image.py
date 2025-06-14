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
		
		for i in range(length):
			for j in range(i + 1, length):
				# swap numbers
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
			
			# reverse the current row
			matrix[i] = matrix[i][::-1]

"""
time complexity:
- O(n^2)

space complexity:
- O(1)
"""