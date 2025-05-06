# name: 1822. sign of the product of an array
# link: https://leetcode.com/problems/sign-of-the-product-of-an-array

# solution #
class Solution:
	def arraySign(self, nums: List[int]) -> int:
		if 0 in nums:
			return 0
		
		neg = sum(1 for num in nums if num < 0)
		
		return 1 if neg % 2 == 0 else -1
	