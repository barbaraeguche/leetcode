# name: 408. valid word abbreviation
# link: https://leetcode.com/problems/valid-word-abbreviation

# solution #
class Solution:
	def validWordAbbreviation(self, word: str, abbr: str) -> bool:
		i, string = 0, ""
		
		while i < len(abbr):
			if abbr[i].isalpha():
				string += abbr[i]
				i += 1
			else:
				temp = ""
				
				while i < len(abbr) and abbr[i].isdigit():
					temp += abbr[i]
					i += 1
				
				# leading zero
				if temp[0] == "0":
					return False
				
				# digit num and string length
				num = int(temp)
				length = len(string)
				
				window = length + num
				
				# digit is greater than total word len
				if window > len(word):
					return False
				
				# idx of running length of digit in abbr
				string += word[length:window]
		
		return string == word
