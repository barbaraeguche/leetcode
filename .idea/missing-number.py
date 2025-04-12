# name: 268. missing number
# link: https://leetcode.com/problems/missing-number

# solution #
class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		length = len(nums)
		
		sum1 = (length * (length + 1)) // 2
		sum2 = sum(nums)
		
		return sum1 - sum2