# name: 844. backspace string compare
# link: https://leetcode.com/problems/backspace-string-compare

# solution #
class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		def imp_stack(text: str) -> str:
			stack = []
			
			for char in text:
				if char == '#' and stack:
					stack.pop()
				else:
					stack.append(char)
			
			return "".join([s for s in stack if s != '#'])
		
		return imp_stack(s) == imp_stack(t)
	