# name: 26. remove duplicates from sorted array
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array

# solution #
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		current, idx = nums[0], 0
		
		for i, num in enumerate(nums[1:]):
			if num == current:
				continue
			else:
				idx += 1
				nums[idx] = num
				current = num
		
		return idx + 1
	