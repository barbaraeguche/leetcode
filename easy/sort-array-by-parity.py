# name: 905. sort array by parity
# link: https://leetcode.com/problems/sort-array-by-parity

# solution #
class Solution:
	def sortArrayByParity(self, nums: List[int]) -> List[int]:
		return (
			[num for num in nums if num % 2 == 0] +
			[num for num in nums if num % 2 == 1]
		)
	