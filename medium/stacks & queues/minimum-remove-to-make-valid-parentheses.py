# name: 1249. minimum remove to make valid parentheses
# link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

# solution #
class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:
		openCount = closeCount = 0
		openStack, closeQueue = [], deque()
		
		# loop 1: iterate from left to right
		for char in s:
			if char == "(":
				openCount += 1
				openStack.append(char)
			
			# must be lesser than seen open brackets
			elif char == ")":
				if closeCount < openCount:
					closeCount += 1
					openStack.append(char)
			
			# english letter
			else:
				openStack.append(char)
		
		# loop 2: iterate from right to left
		while openStack:
			char = openStack.pop()
			
			if char == "(":
				if closeCount < openCount:
					openCount -= 1
					continue
			
			# english letter and close brackets
			closeQueue.appendleft(char)
		
		return "".join(closeQueue)

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""