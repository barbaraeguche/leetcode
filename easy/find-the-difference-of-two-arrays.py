# name: 2215. find the difference of two arrays
# link: https://leetcode.com/problems/find-the-difference-of-two-arrays

# solution #
class Solution:
	def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
		set1 = set(nums1)
		set2 = set(nums2)
		
		return [list(set1.difference(set2)), list(set2.difference(set1))]