# name: 1678. goal parser interpretation
# link: https://leetcode.com/problems/goal-parser-interpretation

# solution #
class Solution:
	def interpret(self, command: str) -> str:
		return command.replace('()', 'o').replace('(al)', 'al')