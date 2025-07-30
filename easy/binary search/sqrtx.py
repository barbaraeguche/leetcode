# name: 69. sqrt(x)
# link: https://leetcode.com/problems/sqrtx

# solution #
class Solution:
	def mySqrt(self, x: int) -> int:
		# edge case
		if x < 2:
			return x
		
		left, right = 2, x // 2
		
		while left <= right:
			mid = (left + right) // 2
			square = mid * mid
			
			# square root found
			if square == x:
				return mid
			
			if square < x:
				left = mid + 1
			else:
				right = mid - 1
		
		return right

"""
time complexity:
- O(log(n))

space complexity:
- O(1)
"""