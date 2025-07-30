# name: 209. minimum size subarray sum
# link: https://leetcode.com/problems/minimum-size-subarray-sum

# solution #
class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		window = float("inf")
		left = subArrSum = 0
		
		for right in range(len(nums)):
			subArrSum += nums[right]
			
			# reduce the window
			while subArrSum - nums[left] >= target:
				subArrSum -= nums[left]
				left += 1
			
			# record min size
			if subArrSum >= target:
				window = min(window, right - left + 1)
		
		return window if window != float("inf") else 0
	
"""
time complexity:
- O(n)

space complexity:
- O(1)
"""