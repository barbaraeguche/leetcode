# name: 3151. special array i
# link: https://leetcode.com/problems/special-array-i

# solution #
class Solution:
	def isArraySpecial(self, nums: List[int]) -> bool:
		def is_special(num1: int, num2: int) -> bool:
			return (
				num1 % 2 == 0 and num2 % 2 != 0 or
				num1 % 2 != 0 and num2 % 2 == 0
			)
		
		for i in range(len(nums) - 1):
			if not is_special(nums[i], nums[i+1]):
				return False
		
		return True
	