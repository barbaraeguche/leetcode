# name: 349. intersection of two arrays
# link: https://leetcode.com/problems/intersection-of-two-arrays

# solution #
class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		return list(set(nums1) & set(nums2))
	