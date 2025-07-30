# name: 59. spiral matrix ii
# link: https://leetcode.com/problems/spiral-matrix-ii

# solution #
class Solution:
	def generateMatrix(self, n: int) -> List[List[int]]:
		currentNum, maximumNum = 1, n * n
		
		left, right = 0, n
		top, bottom = 0, n
		
		matrix = [[0 for _ in range(n)] for _ in range(n)]
		
		while currentNum <= maximumNum:
			# row: left to right
			for i in range(left, right):
				matrix[top][i] = currentNum
				currentNum += 1
			top += 1
			
			# col: top to bottom
			for i in range(top, bottom):
				matrix[i][right - 1] = currentNum
				currentNum += 1
			right -= 1
			
			# to not process an already processed row or column
			if not currentNum <= maximumNum:
				break
			
			# row: right to left
			for i in range(right - 1, left - 1, -1):
				matrix[bottom - 1][i] = currentNum
				currentNum += 1
			bottom -= 1
			
			# col: bottom to top
			for i in range(bottom - 1, top - 1, -1):
				matrix[i][left] = currentNum
				currentNum += 1
			left += 1
		
		return matrix
