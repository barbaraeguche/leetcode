# name: 62. unique paths
# link: https://leetcode.com/problems/unique-paths

# solution #
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		paths = [[1 for _ in range(n)] for _ in range(m)]
		
		for i in range(1, m):
			for j in range(1, n):
				# number of top moves plus that of left
				paths[i][j] = paths[i][j-1] + paths[i-1][j]
			
		# the final path is at the last row-col pair
		return paths[m-1][n-1]

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""