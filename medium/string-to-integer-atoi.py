# name: 8. string to integer (atoi)
# link: https://leetcode.com/problems/string-to-integer-atoi

# solution #
class Solution:
	def myAtoi(self, s: str) -> int:
		string = ""
		
		for i, char in enumerate(s):
			empty = len(string) == 0
			
			if char == " ":
				if empty: continue  # trailing spaces
				else: break
			
			if char in "-+":
				if empty: string += char  # first sign
				else: break
			
			if char.isdigit():
				if char == "0":
					# if next character is not a digit
					if (i + 1) < len(s) and not s[i+1].isdigit():
						string += s[i]
						break
					
					# trailing zeros
					if empty or not any(c in "123456789" for c in string):
						continue
				string += char
			
			# return when encountered an alphabetical character
			if char.isalpha() or char == ".":
				if empty: return 0
				else: break
		
		# if string has only none-numbers
		try:
			_ = int(string)
		except ValueError:
			return 0
		
		# try conversions
		if int(string) < (-2 ** 31):
			return -2 ** 31
		
		if int(string) > ((2 ** 31) - 1):
			return (2 ** 31) - 1
		
		return int(string)
	