# name: 509. fibonacci number
# link: https://leetcode.com/problems/fibonacci-number

# solution #
class Solution:
	def fib(self, n: int) -> int:
		if n < 2: return n
		return self.fib(n - 1) + self.fib(n - 2)
	