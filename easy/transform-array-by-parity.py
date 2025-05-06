# name: 3467. transform array by parity
# link: https://leetcode.com/problems/transform-array-by-parity

# solution #
class Solution:
	def transformArray(self, nums: List[int]) -> List[int]:
		even_count = sum(1 for num in nums if num % 2 == 0)
		odd_count = sum(1 for num in nums if num % 2 != 0)
		
		return ([0] * even_count) + ([1] * odd_count)
	