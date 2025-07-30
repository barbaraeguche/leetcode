# name: 153. find minimum in rotated sorted array
# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

# solution #
class Solution:
	def findMin(self, nums: List[int]) -> int:
		left, right = 0, len(nums) - 1
		
		while left < right:
			mid = (left + right) // 2
			
			# the minimum is in the right part
			if nums[mid] > nums[right]:
				left = mid + 1
				
			# the minimum is in the left part, middle included
			else:
				right = mid
		
		return nums[left]

"""
time complexity:
- O(log(n))

space complexity:
- O(1)
"""