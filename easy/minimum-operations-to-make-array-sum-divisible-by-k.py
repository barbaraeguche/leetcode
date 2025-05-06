# name: 3512. minimum operations to make array sum divisible by k
# link: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k

# solution #
class Solution:
	def minOperations(self, nums: List[int], k: int) -> int:
		return sum(nums) % k
	