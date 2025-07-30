# name: 50. pow(x,n)
# link: https://leetcode.com/problems/powx-n

# solution #
class Solution:
	def myPow(self, x: float, n: int) -> float:
		# edge case
		if n == 0:
			return 1
		
		# negative exponents
		if n < 0:
			n *= -1.0
			x = 1.0 / x
		
		power = 1
		
		while n != 0:
			# make the exponent even, keep track of previous power
			if n % 2 == 1:
				power *= x
				n -= 1
			
			# logarithmic
			x *= x
			n //= 2
		
		return power

"""
time complexity:
- O(log(n))

space complexity:
- O(1)
"""