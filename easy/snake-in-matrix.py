# name: 3248. snake in matrix
# link: https://leetcode.com/problems/snake-in-matrix

# solution #
class Solution:
	def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
		count = 0
		
		for com in commands:
			if com == "UP":
				count -= n
			elif com == "DOWN":
				count += n
			
			elif com == "LEFT":
				count -= 1
			else:
				count += 1
		
		return count
