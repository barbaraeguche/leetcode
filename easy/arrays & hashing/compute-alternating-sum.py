# name: 3701. compute alternating sum
# link: https://leetcode.com/problems/compute-alternating-sum

# solution #
class Solution:
	def alternatingSum(self, nums: List[int]) -> int:
		even = odd = 0
		
		for i, num in enumerate(nums):
			if i % 2:
				odd += num
			else:
				even += num
		
		return even - odd
	
"""
time complexity:
- O(n)

space complexity:
- O(1)
"""