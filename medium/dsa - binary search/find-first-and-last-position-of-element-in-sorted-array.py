# name: 34. find first and last position of element in sorted array
# link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

# solution #
class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		left, right = 0, len(nums) - 1
		start, stop = float('inf'), float('-inf')
		
		# find start position
		while left <= right:
			mid = (left + right) // 2
			num = nums[mid]
			
			if num == target:
				start = min(start, mid)
				right = mid - 1  # to find the minimum
			elif num < target:
				left = mid + 1
			else:
				right = mid - 1
		
		left, right = 0, len(nums) - 1
		
		# find the stop position
		while left <= right:
			mid = (left + right) // 2
			num = nums[mid]
			
			if num == target:
				stop = max(stop, mid)
				left = mid + 1  # to find the maximum
			elif num <= target:
				left = mid + 1
			else:
				right = mid - 1
		
		# if you could not find a start, then you cannot find an end
		if start == float('inf'):
			return [-1, -1]
		
		return [start, stop]
