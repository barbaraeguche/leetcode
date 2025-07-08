# name: 198. house robber
# link: https://leetcode.com/problems/house-robber

# solution #
class Solution:
	def rob(self, nums: List[int]) -> int:
		length = len(nums)
		
		# only two houses to rob
		if length <= 2:
			return max(nums)
		
		for i in range(2, length):
			# rob the prev non-adjacent house
			nums[i] += nums[i-2]
			# update the prev adjacent house
			nums[i-1] = max(nums[i-2], nums[i-1])
		
		# max money is going to be the last two
		return max(nums[-2], nums[-1])

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""