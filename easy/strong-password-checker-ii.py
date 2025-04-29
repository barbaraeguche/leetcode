# name: 2299. strong password checker ii
# link: https://leetcode.com/problems/strong-password-checker-ii

# solution #
class Solution:
	def strongPasswordCheckerII(self, password: str) -> bool:
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		special = "!@#$%^&*()-+"
		digits = "0123456789"
		
		string = alphabets + special + digits
		
		# length check
		if len(password) < 8:
			return False
		
		# lower case check
		if not set(alphabets) & set(password):
			return False
		
		# upper case check
		if not set(alphabets.upper()) & set(password):
			return False
		
		# digit check
		if not any(c.isdigit() for c in password):
			return False
		
		# special character check
		if not set(special) & set(password):
			return False
		
		# adjacent check
		for char in string:
			if char * 2 in password:
				return False
		
		return True
