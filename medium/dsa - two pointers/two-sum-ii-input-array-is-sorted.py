# name: 167. two sum ii input array is sorted
# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# solution #
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		left, right = 0, len(numbers) - 1
		
		while left < right:
			num = numbers[left] + numbers[right]
			
			if num == target:
				return [left + 1, right + 1]
			
			# the summation is too small
			if num < target:
				left += 1
			else:
				right -= 1
		
		return []
	