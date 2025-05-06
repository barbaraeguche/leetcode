# name: 3114. latest time you can obtain after replacing characters
# link: https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters

# solution #
class Solution:
	def findLatestTime(self, s: str) -> str:
		h1, h2, _, m1, m2 = s
		
		# hour formatting
		if h1 == "?" and h2 == "?":
			h1 = h2 = "1"
		elif h1 == "?":
			if 0 <= int(h2) <= 1:
				h1 = "1"
			elif 2 <= int(h2) <= 9:
				h1 = "0"
		elif h2 == "?":
			if int(h1) == 0:
				h2 = "9"
			elif int(h1) == 1:
				h2 = "1"
		
		# minute formatting
		if m1 == "?" and m2 == "?":
			m1 = "5"
			m2 = "9"
		elif m1 == "?":
			m1 = "5"
		elif m2 == "?":
			m2 = "9"
		
		return f"{h1}{h2}:{m1}{m2}"
