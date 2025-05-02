# name: 2855. minimum right shifts to sort the array
# link: https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array

# solution #
class Solution:
	def minimumRightShifts(self, nums: List[int]) -> int:
		is_sorted = list(sorted(nums))
		
		# if is already sorted
		if nums == is_sorted:
			return 0
		
		for i in range(len(nums)):
			nums = [nums[-1]] + nums[:-1]
			
			if nums == is_sorted:
				return i + 1
		
		return -1
