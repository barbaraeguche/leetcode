# name: 485. max consecutive ones
# link: https://leetcode.com/problems/max-consecutive-ones

# solution #
class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		maxCons = count = 0
		
		for num in nums:
			if num == 1:
				count += 1
			else:
				maxCons = max(maxCons, count)
				count = 0  # reset the counter
		
		# for the last value if it where a `1`
		return max(maxCons, count)

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""