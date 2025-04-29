# name: 1614. maximum nesting depth of the parentheses
# link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

# solution #
class Solution:
	def maxDepth(self, s: str) -> int:
		depth = watch = 0
		
		for char in s:
			# increment the depth
			if char == "(":
				depth += 1
			
			# take max of prev nested and current depth
			elif char == ")":
				watch = max(depth, watch)
				depth -= 1  # decrement the depth
		
		return watch
	