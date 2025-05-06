# name: 2224. minimum number of operations to convert time
# link: https://leetcode.com/problems/minimum-number-of-operations-to-convert-time

# solution #
class Solution:
	def convertTime(self, current: str, correct: str) -> int:
		count, total = 0, self.to_minutes(current, correct)
		
		while total > 0:
			if 60 <= total:
				total -= 60
			elif 15 <= total:
				total -= 15
			
			elif 5 <= total:
				total -= 5
			elif 1 <= total:
				total -= 1
			
			count += 1
		
		return count
	
	@staticmethod
	def to_minutes(a: str, b: str) -> int:
		hrs = (int(b[:2]) - int(a[:2])) * 60
		mins = int(b[3:]) - int(a[3:])
		
		return hrs + mins
