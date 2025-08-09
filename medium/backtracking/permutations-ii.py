# name: 47. permutations ii
# link: https://leetcode.com/problems/permutations-ii

# solution #
class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		# sort the array
		nums.sort()
		
		permutations = []
		
		def validPermutations(i):
			# base case
			if i == len(nums):
				permutations.append(nums[:])
				return
			
			for j in range(i, len(nums)):
				# avoid duplicates
				if j > i and nums[i] == nums[j]:
					continue
				
				nums[i], nums[j] = nums[j], nums[i]
				validPermutations(i+1)
			
			for j in range(len(nums) - 1, i, -1):
				nums[i], nums[j] = nums[j], nums[i]
		
		validPermutations(0)
		return permutations

"""
time complexity:
- O(n * n!)

space complexity:
- O(n!)
"""