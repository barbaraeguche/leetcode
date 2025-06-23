# name: 415. add strings
# link: https://leetcode.com/problems/add-strings

# solution #
class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		return self.addNums(num1, num2, "0")
	
	def addNums(self, num1: str, num2: str, carry: str) -> str:
		if not num1 and not num2 and carry == "0":
			return ""
		
		base = ord('0')
		
		# always sum the last values
		n1 = num1[-1] if num1 else "0"
		n2 = num2[-1] if num2 else "0"
		
		# sum of n1 and n2 and carry in an integer format
		calc = (ord(n1) - base) + (ord(n2) - base) + (ord(carry) - base)
		# perform base 10 calculation
		carry, num = divmod(calc, 10)
		
		# perform recursion till last number
		return self.addNums(num1[:-1], num2[:-1], str(carry)) + str(num)

"""
time complexity:
- O(max(n, m)

space complexity:
- O(max(n, m)
"""