# name: 3173. bitwise-or-of-adjacent-elements
# link: https://leetcode.com/problems/bitwise-or-of-adjacent-elements

# solution #
class Solution:
	def orArray(self, nums: List[int]) -> List[int]:
		length = len(nums)
		result = [0] * (length - 1)
		
		for i in range(1, length):
			result[i-1] = nums[i-1] | nums[i]
		
		return result

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""