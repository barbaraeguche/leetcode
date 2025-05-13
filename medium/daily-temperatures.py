# name: 739. daily temperatures
# link: https://leetcode.com/problems/daily-temperatures

# solution #
class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		length = len(temperatures)
		
		stack, array = [], [0] * length
		
		for i in range(length):
			# while the previous temperatures are lower than the current
			while stack and temperatures[stack[-1]] < temperatures[i]:
				popped = stack.pop()
				array[popped] = i - popped
			
			# store the index as reference
			stack.append(i)
		
		return array
