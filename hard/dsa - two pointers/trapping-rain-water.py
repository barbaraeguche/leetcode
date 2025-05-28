# name: 42. trapping rain water
# link: https://leetcode.com/problems/trapping-rain-water

# solution #
class Solution:
	def trap(self, height: List[int]) -> int:
		water, length = 0, len(height)
		
		left, right = [0] * length, [0] * length
		
		# get the prefix and suffix maximum
		for i in range(1, length):
			left[i] = max(left[i-1], height[i-1])
			right[-i-1] = max(right[-i], height[-i])
		
		for i in range(length):
			total = min(left[i], right[i]) - height[i]
			water += total if total > 0 else 0
		
		return water
