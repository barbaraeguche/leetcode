# name: 1283. find the smallest divisor given a threshold
# link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold

# solution #
class Solution:
	def smallestDivisor(self, nums: List[int], threshold: int) -> int:
		# the upper boundary is the max of nums[i]
		left, right = 1, max(nums)
		# maximum possible value
		minDivisor = right
		
		while left <= right:
			mid = (left + right) // 2
			
			# find divisor at current value
			divisor = self.calculateDivisor(nums, mid)
			
			if divisor <= threshold:
				minDivisor = mid
				right = mid - 1
			else:
				left = mid + 1
		
		return minDivisor
	
	def calculateDivisor(self, nums: List[int], rate: int):
		divisor = 0
		
		for num in nums:
			divisor += math.ceil(num / rate)
		
		return divisor
