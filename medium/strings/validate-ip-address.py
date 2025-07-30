# name: 468. validate ip address
# link: https://leetcode.com/problems/validate-ip-address

# solution #
class Solution:
	def validIPAddress(self, queryIP: str) -> str:
		if self.isValidIPv4(queryIP):
			return "IPv4"
		
		if self.isValidIPv6(queryIP):
			return "IPv6"
		
		return "Neither"
	
	@staticmethod
	def isValidIPv4(query: str) -> bool:
		array = query.split(".")
		
		# must be of length 4 after split
		if len(array) != 4:
			return False
		
		for net in array:
			try:
				num = int(net)
			except ValueError:
				return False
			
			# must be in [0, 255]
			if not 0 <= num <= 255:
				return False
			# must not have leading zeros
			if not len(net) == len(str(num)):
				return False
		
		return True
	
	@staticmethod
	def isValidIPv6(query: str) -> bool:
		array = query.split(":")
		
		# must be of length 8 after split
		if len(array) != 8:
			return False
		
		for net in array:
			# must be in [1, 4]
			if not 1 <= len(net) <= 4:
				return False
			# must be a hex string
			if not all(c in '0123456789abcdef' for c in net.lower()):
				return False
		
		return True
