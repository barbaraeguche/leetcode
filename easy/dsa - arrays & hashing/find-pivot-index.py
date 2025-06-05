# name: 724. find pivot index
# link: https://leetcode.com/problems/find-pivot-index

# solution #
class Solution:
	def pivotIndex(self, nums: List[int]) -> int:
		length = len(nums)
		
		left = [nums[0]] * length
		right = [nums[-1]] * length
		
		# take the prefix sums
		for i in range(1, length):
			left[i] = left[i-1] + nums[i]
			right[-i-1] = right[-i] + nums[-i-1]
		
		# pivot index is index where left and right are equal
		for i in range(len(left)):
			if left[i] == right[i]:
				return i
		
		return -1
	