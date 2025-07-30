# name: 367. valid perfect square
# link: https://leetcode.com/problems/valid-perfect-square

# solution #
class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		# edge case
		if num == 1:
			return True
		
		left, right = 2, num // 2
		
		while left <= right:
			mid = (left + right) // 2
			square = mid * mid
			
			# valid perfect square found
			if square == num:
				return True
			
			if square < num:
				left = mid + 1
			else:
				right = mid - 1
		
		return False

"""
time complexity:
- O(log(n))

space complexity:
- O(1)
"""