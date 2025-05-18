# name: 119. pascal's triangle ii
# link: https://leetcode.com/problems/pascals-triangle-ii

# solution #
class Solution:
	def getRow(self, rowIndex: int) -> List[int]:
		triangle = [[1], [1, 1]]
		
		if rowIndex < 2:
			return triangle[rowIndex]
		
		for i in range(3, rowIndex + 2):
			# array of the previous height
			last = triangle[-1]
			# array of the current height
			temp = [1] * i
			
			for j in range(1, i - 1):
				temp[j] = last[j-1] + last[j]
			
			# append current height to list
			triangle.append(temp)
		
		return triangle[rowIndex]
