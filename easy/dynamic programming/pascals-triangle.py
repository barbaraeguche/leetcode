# name: 118. pascal's triangle
# link: https://leetcode.com/problems/pascals-triangle

# solution #
class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		triangle = [[1], [1, 1]]
		
		if numRows < 3:
			return triangle[:numRows]
		
		for i in range(3, numRows + 1):
			# array of the previous height
			last = triangle[-1]
			# array of the current height
			temp = [1] * i
			
			for j in range(1, i - 1):
				temp[j] = last[j-1] + last[j]
			
			# append current height to list
			triangle.append(temp)
		
		return triangle
