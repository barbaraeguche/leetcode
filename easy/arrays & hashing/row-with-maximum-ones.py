# name: 2643. row with maximum ones
# link: https://leetcode.com/problems/row-with-maximum-ones

# solution #
class Solution:
	def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
		idx = count = 0
		
		for i in range(len(mat) - 1, -1, -1):
			oneCnt = 0
			
			for j in range(len(mat[0])):
				oneCnt += 1 if mat[i][j] == 1 else 0
			
			idx = i if count <= oneCnt else idx
			count = max(count, oneCnt)
		
		return [idx, count]
	
"""
time complexity:
- O(n * m)

space complexity:
- O(1)
"""