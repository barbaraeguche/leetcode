# name: 90. subsets ii
# link: https://leetcode.com/problems/subsets-ii

# solution #
class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		# sort the array
		nums.sort()
		
		subSets = []
		
		def validSubsets(idx: int, temp: List[int]) -> None:
			# base case
			if idx == len(nums):
				subSets.append(temp[:])
				return
			
			# take the current num
			temp.append(nums[idx])
			validSubsets(idx + 1, temp)
			# skip the current num
			temp.pop()
			
			# avoid duplicates
			while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
				idx += 1
			
			# move to the next num
			validSubsets(idx + 1, temp)
		
		validSubsets(0, [])
		return subSets

"""
time complexity:
- O(n * 2^n); for each number there are 2^n possible subsets

space complexity:
- O(n)
"""