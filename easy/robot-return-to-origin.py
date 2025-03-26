# name: 657. robot return to origin
# link: https://leetcode.com/problems/robot-return-to-origin

# solution #
class Solution:
	def judgeCircle(self, moves: str) -> bool:
		U, D = moves.count('U'), moves.count('D')
		L, R = moves.count('L'), moves.count('R')
		
		return [R-L, U-D] == [0, 0]