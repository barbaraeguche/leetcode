# name: 77. combinations
# link: https://leetcode.com/problems/combinations

# solution #
class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		combinations = []
		
		def validCombination(idx: int, path: List[int]):
			# combination of size k
			if len(path) == k:
				combinations.append(path[:])
				return
			
			for i in range(idx, n+1):
				# take current num
				path.append(i)
				
				# find all possible combinations
				validCombination(i+1, path)
				# backtrack
				path.pop()
		
		validCombination(1, [])
		return combinations

"""
time complexity:
- O(k * c(n, k)); c(n,k) is the combination formula

space complexity:
- O(c(n, k))
"""