# name: 1413. minimum value to get positive step by step sum
# link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum

# solution #
class Solution:
	def minStartValue(self, nums: List[int]) -> int:
		length = len(nums)
		prefix = [nums[0]] * length
		
		for i in range(1, length):
			prefix[i] = prefix[i-1] + nums[i]
		
		minVal = min(prefix)
		return 1 if minVal >= 1 else abs(minVal) + 1

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""