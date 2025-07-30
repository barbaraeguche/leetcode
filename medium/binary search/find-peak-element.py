# name: 162. find peak element
# link: https://leetcode.com/problems/find-peak-element

# solution #
class Solution:
	def findPeakElement(self, nums: List[int]) -> int:
		l, r = 0, len(nums) - 1
		
		while l <= r:
			mid = (l + r) // 2
			num = nums[mid]
			
			if mid > 0 and nums[mid - 1] > num:
				r = mid - 1
			elif mid < len(nums) - 1 and num < nums[mid + 1]:
				l = mid + 1
			else:
				return mid
		
		return -1
