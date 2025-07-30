# name: 303. range sum query immutable
# link: https://leetcode.com/problems/range-sum-query-immutable

# solution #
class NumArray:
	
	def __init__(self, nums: List[int]):
		length = len(nums) + 1
		self.nums = [0] * length
		
		for i in range(1, length):
			self.nums[i] = self.nums[i-1] + nums[i-1]
	
	def sumRange(self, left: int, right: int) -> int:
		return self.nums[right + 1] - self.nums[left]

"""
time complexity:
- O(n) for init
- O(1) for sumRange

space complexity:
- O(n)
"""