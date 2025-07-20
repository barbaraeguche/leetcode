# name: 38. count and say
# link: https://leetcode.com/problems/count-and-say

# solution #
class Solution:
	def countAndSay(self, n: int) -> str:
		runLength = "1"
		
		for _ in range(2, n+1):
			runLength = self.encoding(runLength)
		
		return runLength
	
	def encoding(self, num: str):
		count, current = 1, num[0]
		# keep track of run length
		countArr = []
		
		for digit in num[1:]:
			if digit == current:
				# run length
				count += 1
			else:
				# different number
				countArr.append(f"{count}{current}")
				# reset variables
				count, current = 1, digit
		
		# append the last run length
		countArr.append(f"{count}{current}")
		
		return "".join(countArr)

"""
time complexity:
- O(2^n)

space complexity:
- O(2^n)
"""