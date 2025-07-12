# name: 498. diagonal traverse
# link: https://leetcode.com/problems/diagonal-traverse

# solution #
class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		rows, cols = len(mat), len(mat[0])
		
		# for each diagonal
		bucket = [[] for _ in range(rows + cols - 1)]
		
		for i in range(rows):
			for j in range(cols):
				# i+j is the diagonal index
				bucket[i+j].append(mat[i][j])
		
		result = []
		
		for i in range(len(bucket)):
			buck = bucket[i]
			
			# even indices should be reversed
			if not i % 2:
				buck.reverse()
			
			# extend to result array
			result.extend(buck)
		
		return result

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""