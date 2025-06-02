# name: 1472. design browser history
# link: https://leetcode.com/problems/design-browser-history

# solution #
class BrowserHistory:
	
	def __init__(self, homepage: str):
		self.index = 0
		self.history = []
		
		# append the current page
		self.history.append(homepage)
	
	def visit(self, url: str) -> None:
		# last history
		if self.index == len(self.history) - 1:
			self.history.append(url)
		else:
			# a case where you're visiting a new page rather than going forward
			self.history = self.history[:self.index + 1] + [url]
		
		self.index += 1
	
	def back(self, steps: int) -> str:
		# to prevent out of bounds error
		self.index = max(self.index - steps, 0)
		return self.history[self.index]
	
	def forward(self, steps: int) -> str:
		# to prevent out of bounds error
		self.index = min(self.index + steps, len(self.history) - 1)
		return self.history[self.index]
