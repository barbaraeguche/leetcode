# name: 1507. reformat date
# link: https://leetcode.com/problems/reformat-date

# solution #
class Solution:
	def reformatDate(self, date: str) -> str:
		d, m, y = date.split()
		
		month_map = {
			"Jan": "1", "Feb": "2", "Mar": "3", "Apr": "4",
			"May": "5", "Jun": "6", "Jul": "7", "Aug": "8",
			"Sep": "9", "Oct": "10", "Nov": "11", "Dec": "12"
		}
		
		d = "".join(filter(str.isdigit, d)).rjust(2, '0')
		m = month_map[m].rjust(2, '0')
		
		return f"{y}-{m}-{d}"
	