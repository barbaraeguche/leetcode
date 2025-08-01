# name: 33. search in rotated sorted array
# link: https://leetcode.com/problems/search-in-rotated-sorted-array

# solution #
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left, right = 0, len(nums) - 1
		
		while left <= right:
			mid = (left + right) // 2
			
			# found the target
			if target == nums[mid]:
				return mid
			
			# check in the left sorted part
			if nums[left] <= nums[mid]:
				if target < nums[left] or target > nums[mid]:
					left = mid + 1
				else:
					right = mid - 1
			
			# check in the right sorted part
			else:
				if target > nums[right] or target < nums[mid]:
					right = mid - 1
				else:
					left = mid + 1
		
		return -1

"""
time complexity:
- O(log(n))

space complexity:
- O(1)
"""