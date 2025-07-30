# name: 268. missing number
# link: https://leetcode.com/problems/missing-number

# solution #
class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		n = len(nums)
		
		formal = (n * (n + 1)) // 2
		summation = sum(nums)
		
		return formal - summation
	
"""
time complexity:
- O(1)

space complexity:
- O(1)
"""