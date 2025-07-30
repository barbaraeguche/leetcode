# name: 1572. matrix diagonal sum
# link: https://leetcode.com/problems/matrix-diagonal-sum

# solution #
class Solution:
	def diagonalSum(self, mat: List[List[int]]) -> int:
		rows = len(mat)
		
		primaryDiag = sum(mat[i][i] for i in range(rows))
		secondaryDiag = sum(mat[i][rows - i - 1] for i in range(rows))
		
		diagSum = primaryDiag + secondaryDiag
		
		# no overlapping diagonals
		if rows % 2 == 0:
			return diagSum
		
		duplicate = rows // 2
		return diagSum - mat[duplicate][duplicate]

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""