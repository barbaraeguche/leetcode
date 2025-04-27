# name: 796. rotate string
# link: https://leetcode.com/problems/rotate-string

# solution #
class Solution:
	def rotateString(self, s: str, goal: str) -> bool:
		if len(s) != len(goal):
			return False
		
		length = len(goal)
		
		for g in range(length):
			s = s[1:] + s[0]
			
			if s == goal:
				return True
			
			if g == length - 1:
				return False
		
		return False
	
	def rotateString(self, s: str, goal: str) -> bool:
		if len(s) != len(goal):
			return False
		
		return s in goal + goal
	