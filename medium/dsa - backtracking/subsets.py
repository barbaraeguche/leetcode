# name: 78. subsets
# link: https://leetcode.com/problems/subsets

# solution #
class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		temp, subSets = [], []
		
		def backtrack(idx: int):
			# base case
			if idx == len(nums):
				subSets.append(temp[:])
				return
			
			# take the current num
			temp.append(nums[idx])
			backtrack(idx + 1)
			
			# skip the current num
			temp.pop()
			backtrack(idx + 1)
		
		backtrack(0)
		return subSets

"""
time complexity:
- O(n * 2^n); for each number there are 2^n possible subsets

space complexity:
- O(2^n)
"""