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
	