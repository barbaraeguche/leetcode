# name: 485. max consecutive ones
# link: https://leetcode.com/problems/max-consecutive-ones

# solution #
class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		nums = "".join(str(num) for num in nums)
		splitted = nums.split('0')
		
		return len(max(splitted))