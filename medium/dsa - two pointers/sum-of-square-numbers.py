# name: 633. sum of square numbers
# link: https://leetcode.com/problems/sum-of-square-numbers

# solution #
class Solution:
	def judgeSquareSum(self, c: int) -> bool:
		left, right = 0, ceil(sqrt(c))
		
		while left <= right:
			a, b = (left ** 2), (right ** 2)
			square = a + b
			
			# valid square sum found
			if square == c:
				return True
			
			if square < c:
				left += 1
			else:
				right -= 1
		
		return False

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""