# name: 66. plus one
# link: https://leetcode.com/problems/plus-one

# solution #
class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		n = len(digits)
		
		# loop backwards
		for i in range(n - 1, -1, -1):
			# addition will not go over 9
			if digits[i] < 9:
				digits[i] += 1
				# no need to continue
				return digits
			
			# digits[i] == 0, so there will be an overflow
			digits[i] = 0
		
		# [1] for the overflow
		return [1] + digits

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""