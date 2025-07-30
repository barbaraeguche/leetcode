# name: 496. next greater element i
# link: https://leetcode.com/problems/next-greater-element-i

# solution #
class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		# for better indexing
		nums1Map = {val: idx for idx, val in enumerate(nums1)}
		greater, stack = [-1] * len(nums1), []
		
		for idx in range(len(nums2)):
			while stack and nums2[stack[-1]] < nums2[idx]:
				num = nums2[stack.pop()]
				
				# if present in nums1, store the next greater value
				if num in nums1Map:
					greater[nums1Map[num]] = nums2[idx]
			
			stack.append(idx)
		
		return greater
