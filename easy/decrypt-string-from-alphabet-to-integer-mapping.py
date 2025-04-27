# name: 1309. decrypt string from alphabet to integer mapping
# link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping

# solution #
class Solution:
	def freqAlphabets(self, s: str) -> str:
		string, s = "", s[::-1]
		
		while s:
			char = s[0]
			
			if char == '#':
				# read from left to right, get num value
				word = f"{s[2]}{s[1]}"
				num = int(word) - 1
				
				# get chr value, move past read nums
				string = f"{chr(ord('a') + num)}{string}"
				s = s[3:]
			
			else:
				num = int(char) - 1
				string = f"{chr(ord('a') + num)}{string}"
				s = s[1:]
		
		return string
	