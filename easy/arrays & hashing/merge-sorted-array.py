# name: 88. merge sorted array
# link: https://leetcode.com/problems/merge-sorted-array

# solution #
class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		index1, index2 = m - 1, n - 1
		# start from the end
		position = m + n - 1
		
		# sort both arrays
		while index1 >= 0 and index2 >= 0:
			n1, n2 = nums1[index1], nums2[index2]
			
			if n1 >= n2:
				nums1[position] = n1
				index1 -= 1
			else:
				nums1[position] = n2
				index2 -= 1
			
			position -= 1
		
		"""
		note: this is not called for nums1 as it's the array we are replenishing
		"""
		# replenish nums1 with values in nums2
		while position >= 0 and index2 >= 0:
			nums1[position] = nums2[index2]
			position, index2 = position - 1, index2 - 1

"""
time complexity:
- O(n + m)

space complexity:
- O(1)
"""