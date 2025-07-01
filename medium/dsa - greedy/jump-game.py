# name: 55. jump game
# link: https://leetcode.com/problems/jump-game

# solution #
class Solution:
	def canJump(self, nums: List[int]) -> bool:
		length = len(nums)
		# base target is the last index
		target = length - 1
		
		# loop back and see if you can jump to target
		for i in range(length - 2, -1, -1):
			# if you can jump, set target to current index
			if i + nums[i] >= target:
				target = i
		
		# target will be the 0-th index if you can reach the end
		return target == 0

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""