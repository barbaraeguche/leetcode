# name: 551. student attendance record i
# link: https://leetcode.com/problems/student-attendance-record-i

# solution #
class Solution:
	def checkRecord(self, s: str) -> bool:
		return s.count('A') < 2 and s.count('LLL') == 0