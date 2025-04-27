# name: 682. baseball game
# link: https://leetcode.com/problems/baseball-game

# solution #
class Solution:
	def calPoints(self, operations: List[str]) -> int:
		nums: List[int] = []
		
		for i, op in enumerate(operations):
			if op == 'C':
				nums.pop()
			
			elif op == 'D':
				nums.append(nums[-1] * 2)
			
			elif op == '+':
				nums.append(nums[-1] + nums[-2])
			
			else: nums.append(int(op))
		
		return sum(nums)
	