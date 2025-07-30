# name: 1185. day of the week
# link: https://leetcode.com/problems/day-of-the-week

# solution #
class Solution:
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
		# note: january 1st 1971 was a friday
		months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		weekHash = {
			2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday", 0: "Friday", 1: "Saturday"
		}
		
		# year in days
		days = (year - 1971) * 365
		
		# month in days
		for i in range(month - 1):
			days += months[i]
		
		# day since the month started(today not inclusive)
		days += day - 1
		# leap year count
		days += self.countLeapYears(year)
		
		# month needs to be from march if the current year is a leap year
		if self.isLeapYear(year) and month <= 2:
			days -= 1
		
		return weekHash[days % 7]
	
	def countLeapYears(self, year: int) -> int:
		leapYears = 0
		
		# count leap years from 1972 till current year
		for yr in range(1972, year + 1, 4):
			leapYears += 1 if self.isLeapYear(yr) else 0
		
		return leapYears
	
	def isLeapYear(self, yr: int) -> bool:
		if (yr % 400 == 0) and (yr % 100 == 0):
			return True
		elif (yr % 4 == 0) and (yr % 100 != 0):
			return True
		
		return False
	
"""
time complexity:
- O(n)

space complexity:
- O(1)
"""