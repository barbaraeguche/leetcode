# name: 1797. design authentication manager
# link: https://leetcode.com/problems/design-authentication-manager

# solution #
class AuthenticationManager:
	
	def __init__(self, timeToLive: int):
		self.timeToLive = timeToLive
		self.authMap = defaultdict(int)
	
	def generate(self, tokenId: str, currentTime: int) -> None:
		tokCurrTime = self.authMap.get(tokenId, -1)
		
		# unique token
		if tokCurrTime == -1:
			self.authMap[tokenId] = currentTime
	
	def renew(self, tokenId: str, currentTime: int) -> None:
		tokCurrTime = self.authMap.get(tokenId, -1)
		
		# invalid token
		if tokCurrTime == -1:
			return None
		
		# check if the token became invalid
		if (tokCurrTime + self.timeToLive) <= currentTime:
			del self.authMap[tokenId]
			return None
		
		# renew the token
		self.authMap[tokenId] = currentTime
		return None
	
	def countUnexpiredTokens(self, currentTime: int) -> int:
		unexpired = 0
		
		for _, currTime in self.authMap.items():
			if (currTime + self.timeToLive) > currentTime:
				unexpired += 1
		
		return unexpired

"""
time complexity:
- init, generate, renew: O(1)
- countUnexpiredTokens: O(n)

space complexity:
- O(n)
"""