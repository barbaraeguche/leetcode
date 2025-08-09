# name: 46. permutations
# link: https://leetcode.com/problems/permutations

# solution #
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		permutations = []
		
		def validPermutations(i):
			# base case
			if i == len(nums):
				permutations.append(nums[:])
				return
			
			for j in range(i, len(nums)):
				nums[i], nums[j] = nums[j], nums[i]
				validPermutations(i+1)
				nums[i], nums[j] = nums[j], nums[i]
		
		validPermutations(0)
		return permutations

"""
time complexity:
- O(n * n!)

space complexity:
- O(n!)
"""