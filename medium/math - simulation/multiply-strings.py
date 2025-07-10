# name: 43. multiply strings
# link: https://leetcode.com/problems/multiply-strings

# solution #
class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		n, m = len(num1), len(num2)
		
		base, finalNum = ord('0'), 0
		
		def multiplyNum(i, n2, carry, pad):
			if i < 0:
				return carry * 10 ** pad
			
			# summation of all three numbers
			summation = (ord(num1[i]) - base) * (ord(n2) - base) + carry
			carry, value = divmod(summation, 10)
			
			padding = 10 ** pad
			
			# running multiplication
			number = value * padding
			return multiplyNum(i - 1, n2, carry, pad + 1) + number
		
		for j in range(m - 1, -1, -1):
			padding = 10 ** (m - j - 1)
			
			# multiple backwards
			multNum = multiplyNum(n - 1, num2[j], 0, 0)
			# running total
			finalNum += multNum * padding
		
		return str(finalNum)

"""
time complexity:
- O(n * m); n is the length of num1, m is the length of num2

space complexity:
- O(n * m)
"""