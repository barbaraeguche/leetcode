# name: 394. decode string
# link: https://leetcode.com/problems/decode-string

# solution #
class Solution:
	def decodeString(self, s: str) -> str:
		stack = []
		
		for char in s:
			if char == "]":
				queue = deque()  # for O(1) addition
				
				# reform the letters
				while stack and stack[-1] != "[":
					queue.appendleft(stack.pop())
				
				# remove open bracket
				stack.pop()
				
				i = number = 0
				
				# get the number
				while stack and stack[-1].isdigit():
					number = 10 ** i * int(stack.pop()) + number
					i += 1
				
				# decode the encoding
				newStr = "".join(queue) * number
				# add back to stack
				stack.append(newStr)
				continue
			
			stack.append(char)
		
		return "".join(stack)

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""