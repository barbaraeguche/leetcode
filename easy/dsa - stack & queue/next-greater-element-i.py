# name: 496. next greater element i
# link: https://leetcode.com/problems/next-greater-element-i

# solution #
class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		greater, stack = [-1] * len(nums1), []
		
		for idx, num in enumerate(nums2):
			while stack and nums2[stack[-1][0]] < num:
				_, n = stack.pop()
				
				# find the idx in nums1
				if n in nums1:
					greater[nums1.index(n)] = num
			
			# store as (idx, num)
			stack.append((idx, num))
		
		return greater
