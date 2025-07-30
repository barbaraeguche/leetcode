# name: 560. subarray sum equals k
# link: https://leetcode.com/problems/subarray-sum-equals-k

# solution #
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		sumMap = { 0:1 }
		subSum = totalSum = 0
		
		for num in nums:
			totalSum += num
			prefixSum = totalSum - k
			
			subSum += sumMap.get(prefixSum, 0)
			sumMap[totalSum] = 1 + sumMap.get(totalSum, 0)
		
		return subSum

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""