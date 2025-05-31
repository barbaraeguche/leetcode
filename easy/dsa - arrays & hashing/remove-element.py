# name: 27. remove element
# link: https://leetcode.com/problems/remove-element

# solution #
class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		idx = 0
		
		for num in nums:
			if num != val:
				nums[idx] = num
				idx += 1
		
		return idx
	