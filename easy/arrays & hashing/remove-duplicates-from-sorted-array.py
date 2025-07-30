# name: 26. remove duplicates from sorted array
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array

# solution #
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		idx = 1
	
		for i, num in enumerate(nums[1:], 1):
			if nums[i] != nums[i-1]:
				nums[idx] = num
				idx += 1
		
		return idx
	