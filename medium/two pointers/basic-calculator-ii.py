# name: 227. basic calculator ii
# link: https://leetcode.com/problems/basic-calculator-ii

# solution #
class Solution:
	def calculate(self, s: str) -> int:
		n, oper = len(s), "+"
		
		# basically a two-pointer question
		result = prevNum = currNum = 0
		
		for i, ch in enumerate(s):
			if ch.isdigit():
				# convert to number
				currNum = currNum * 10 + ord(ch) - ord("0")
			
			# an operator or the last number to process
			if (not ch.isdigit() and ch != " ") or i == n - 1:
				if oper == "+":
					result += prevNum
					prevNum = currNum
				elif oper == "-":
					result += prevNum
					prevNum = -currNum  # change the sign
				
				elif oper == "/":
					prevNum = int(prevNum / currNum)  # truncate towards zero
				elif oper == "*":
					prevNum *= currNum
				
				# reset variables
				oper, currNum = ch, 0
		
		return result + prevNum

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""