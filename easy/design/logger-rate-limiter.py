# name: 359. logger rate limiter
# link: https://leetcode.com/problems/logger-rate-limiter

# solution #
class Logger:
	
	def __init__(self):
		self.logMap = {}
	
	def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
		# first time seeing the message
		if not message in self.logMap:
			self.logMap[message] = timestamp
			return True
		
		# last seen >= 10 secs ago
		if self.logMap[message] + 10 <= timestamp:
			self.logMap[message] = timestamp
			return True
		
		return False

"""
time complexity:
- O(1)

space complexity:
- O(m); m is the number of unique messages
"""