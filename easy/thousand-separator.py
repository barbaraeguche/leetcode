# name: 1556. thousand separator
# link: https://leetcode.com/problems/thousand-separator

# solution #
class Solution:
	def thousandSeparator(self, n: int) -> str:
		string = str(n)
		length = len(string)
		
		if length < 3:
			return string
		
		mod = length % 3
		not_mult = mod != 0
		
		splitted = [string[i:i+3] for i in range(mod, length, 3)]
		
		if not_mult:
			splitted = [string[:mod]] + splitted
		
		return ".".join(splitted)
	
	def thousandSeparator(self, n: int) -> str:
		string = str(n)
		
		if len(string) <= 3:
			return string
		
		rem = len(string) % 3
		array = [string[i:i+3] for i in range(rem, len(string), 3)]
		
		if rem != 0:
			array = [string[:rem]] + array
		
		return ".".join(array)
	