# name: 509. fibonacci number
# link: https://leetcode.com/problems/fibonacci-number

# solution #
class Solution:
	def fib(self, n: int) -> int:
		if n < 2: return n
		return self.fib(n - 1) + self.fib(n - 2)
	
	def fib(self, n: int) -> int:
		memo = { 2:1 }
	
		def call(n: int) -> int:
			if n <= 2:
				return memo[2]
			
			if n in memo:
				return memo[n]
			
			memo[n] = self.fib(n - 1) + self.fib(n - 2)
			return memo[n]
		
		return call(n)
