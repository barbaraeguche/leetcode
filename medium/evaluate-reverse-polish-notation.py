# name: 150. evaluate reverse polish notation
# link: https://leetcode.com/problems/evaluate-reverse-polish-notation

# solution #
class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		
		for tok in tokens:
			if tok not in ["*", "/", "-", "+"]:
				stack.append(int(tok))
			
			else:
				val2, val1 = stack.pop(), stack.pop()
				
				if tok == "*":
					stack.append(val1 * val2)
				elif tok == "/":
					stack.append(int(val1 / val2))
				elif tok == "+":
					stack.append(val1 + val2)
				elif tok == "-":
					stack.append(val1 - val2)
		
		return stack[0]
