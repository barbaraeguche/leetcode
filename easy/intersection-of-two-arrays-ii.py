# name: 350. intersection of two arrays ii
# link: https://leetcode.com/problems/intersection-of-two-arrays-ii

# solution #
class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		arr = []
		
		for num in nums1:
			if num in nums2:
				# find the index and remove
				idx = nums2.index(num)
				nums2 = nums2[:idx] + nums2[idx+1:]
				
				# append to list
				arr.append(num)
		
		return arr