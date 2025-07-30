# name: 2614. prime in diagonal
# link: https://leetcode.com/problems/prime-in-diagonal

# solution #
from math import isqrt

class Solution:
	def diagonalPrime(self, nums: List[List[int]]) -> int:
		rows, maxPrime = len(nums), 0
		
		for i in range(rows):
			left, right = nums[i][i], nums[i][rows - i - 1]
			
			if self.isPrime(left):
				maxPrime = max(maxPrime, left)
			if self.isPrime(right):
				maxPrime = max(maxPrime, right)
		
		return maxPrime
	
	def isPrime(self, num: int) -> bool:
		if num <= 1:
			return False
		if num <= 3:
			return True
		if num % 2 == 0 or num % 3 == 0:
			return False
		
		# skip even numbers and multiples of 3 for efficiency
		for i in range(5, isqrt(num) + 1, 6):
			if num % i == 0 or num % (i + 2) == 0:
				return False
		
		return True

"""
time complexity:
- O(n * √M); n is the number of elements, M is the maximum possible diagonal element

space complexity:
- O(1)
"""