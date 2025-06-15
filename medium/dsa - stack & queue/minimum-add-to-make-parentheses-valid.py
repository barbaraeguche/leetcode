# name: 921. minimum add to make parentheses valid
# link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

# solution #
class Solution:
	def minAddToMakeValid(self, s: str) -> int:
		count, stack = 0, []
		
		for char in s:
			if char == "(":
				count += 1
				stack.append(char)
			else:
				# if there is a corresponding open bracket
				if stack:
					count -= 1
					stack.pop()
				else:
					# missing a corresponding open bracket
					count += 1
		
		return count

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""