# name: 2574. left and right sum differences
# link: https://leetcode.com/problems/left-and-right-sum-differences

# solution #
class Solution:
	def leftRightDifference(self, nums: List[int]) -> List[int]:
		length = len(nums)
		
		left_sum = [0] * length
		right_sum = [0] * length
		
		for i in range(1, length):
			left_sum[i] = left_sum[i-1] + nums[i-1]
			right_sum[-i-1] = right_sum[-i] + nums[-i]
		
		for i in range(length):
			left_sum[i] = abs(left_sum[i] - right_sum[i])
		
		return left_sum
	