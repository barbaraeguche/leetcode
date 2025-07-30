# name: 2965. find missing and repeated values
# link: https://leetcode.com/problems/find-missing-and-repeated-values

# solution #
class Solution:
	def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
		n = len(grid)
		
		result = [0] * 2
		# each number in (n * n)
		numArr = [-1] * (n * n)
		
		for i in range(n):
			for j in range(n):
				num = grid[i][j]
				
				# duplicate number
				if numArr[num - 1] != -1:
					result[0] = num
					continue
				
				# keep track of number
				numArr[num - 1] = num
		
		# look for missing number
		for i in range(1, (n * n) + 1):
			if numArr[i-1] == -1:
				result[1] = i
		
		return result
	
"""
time complexity:
- O(n^2)

space complexity:
- O(n^2)
"""