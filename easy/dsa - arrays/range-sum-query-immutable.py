# name: 303. range sum query immutable
# link: https://leetcode.com/problems/range-sum-query-immutable

# solution #
class NumArray:
	
	def __init__(self, nums: List[int]):
		self.nums = nums
	
	def sumRange(self, left: int, right: int) -> int:
		return sum(self.nums[left:right + 1])