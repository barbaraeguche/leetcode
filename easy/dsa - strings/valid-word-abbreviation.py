# name: 408. valid word abbreviation
# link: https://leetcode.com/problems/valid-word-abbreviation

# solution #
class Solution:
	def validWordAbbreviation(self, word: str, abbr: str) -> bool:
		idx, string = 0, ""
		
		while idx < len(abbr):
			if abbr[idx].isalpha():
				string += abbr[idx]
				idx += 1
			
			else:
				cnt = currNum = 0
				
				while idx < len(abbr) and abbr[idx].isdigit():
					currNum = currNum * 10 + ord(abbr[idx]) - ord("0")
					cnt, idx = cnt + 1, idx + 1
					
					# leading zero
					if cnt == 1 and currNum == 0:
						return False
				
				length = len(string)
				window = currNum + length
				
				# cannot be an abbreviation
				if window > len(word):
					return False
				
				# idx of running length of digit in abbr
				string += word[length:window]
		
		return string == word

"""
time complexity:
- O(n + m)

space complexity:
- O(1)
"""