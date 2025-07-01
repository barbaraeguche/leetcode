# name: 1154. day of the year
# link: https://leetcode.com/problems/day-of-the-year

# solution #
class Solution:
	def dayOfYear(self, date: str) -> int:
		yr, m, d = map(int, date.split("-"))
		days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		
		total = 0
		
		for i in range(m - 1):
			total += days[i]
		
		total += d
		
		if self.is_leap_year(yr) and m > 2:
			total += 1
		
		return total
	
	@staticmethod
	def is_leap_year(yr: int) -> bool:
		if (yr % 400 == 0) and (yr % 100 == 0):
			return True
		elif (yr % 4 == 0) and (yr % 100 != 0):
			return True
		
		return False
	