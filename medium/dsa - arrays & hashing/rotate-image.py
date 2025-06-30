# name: 48. rotate image
# link: https://leetcode.com/problems/rotate-image

# solution #
class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		length = len(matrix)
		
		for i in range(length):
			# transpose numbers
			for j in range(i + 1, length):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
				
			# reverse numbers
			for j in range(length // 2):
				matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

"""
time complexity:
- O(n^2)

space complexity:
- O(1)
"""