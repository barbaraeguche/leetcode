# name: 2540. minimum common value
# link: https://leetcode.com/problems/minimum-common-value

# solution #
class Solution:
	def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
		arr = list(set(nums1) & set(nums2))
		
		# sort the array
		arr.sort()
		
		return -1 if len(arr) == 0 else arr[0]
	