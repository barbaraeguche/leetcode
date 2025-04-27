# name: 2535. difference between element sum and digit sum of an array
# link: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

# solution #
class Solution:
	def differenceOfSum(self, nums: List[int]) -> int:
		element = sum(nums)
		digit = sum(int(d) for num in nums for d in str(num))
		
		return abs(element - digit)
	