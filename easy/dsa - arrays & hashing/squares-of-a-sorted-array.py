# name: 977. squares of a sorted array
# link: https://leetcode.com/problems/squares-of-a-sorted-array

# solution #
class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		for i, num in enumerate(nums):
			nums[i] = num ** 2
		
		# sort nums
		nums.sort()
		
		return nums
	
	def sortedSquares(self, nums: List[int]) -> List[int]:
		n = len(nums)
		result = [0] * n
		
		left, right = 0, n - 1
		position = n - 1
		
		# use binary search
		while left <= right:
			n1, n2 = nums[left], nums[right]
			
			if abs(n1) >= abs(n2):
				result[position] = n1 ** 2
				left += 1
			else:
				result[position] = n2 ** 2
				right -= 1
			
			position -= 1
		
		return result
