# name: 1736. latest time by replacing hidden digits
# link: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits

# solution #
class Solution:
	def maximumTime(self, time: str) -> str:
		splitted = time.split(":")
		h1, h2 = splitted[0][0], splitted[0][-1]
		m1, m2 = splitted[1][0], splitted[1][-1]
		
		# hour formatting
		if h1 == "?" and h2 == "?":
			h1 = "2"
			h2 = "3"
		elif h1 == "?":
			if 0 <= int(h2) <= 3:
				h1 = "2"
			elif 4 <= int(h2) <= 9:
				h1 = "1"
		elif h2 == "?":
			if 0 <= int(h1) <= 1:
				h2 = "9"
			elif int(h1) == 2:
				h2 = "3"
		
		# minute formatting
		if m1 == "?" and m2 == "?":
			m1 = "5"
			m2 = "9"
		elif m1 == "?":
			m1 = "5"
		elif m2 == "?":
			m2 = "9"
		
		return f"{h1}{h2}:{m1}{m2}"