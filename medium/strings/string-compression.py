# name: 443. string compression
# link: https://leetcode.com/problems/string-compression

# solution #
class Solution:
	def compress(self, chars: List[str]) -> int:
		charCount, currChar, compWord = 0, chars[0], ""
		
		for i, char in enumerate(chars):
			if char == currChar:
				charCount += 1
			else:
				# perform compression
				compWord += f"{currChar}{charCount if charCount > 1 else ''}"
				
				# reset the variables
				charCount, currChar = 1, char
			
			# last compression
			if i == len(chars) - 1:
				compWord += f"{currChar}{charCount if charCount > 1 else ''}"
		
		# store in the initial array
		for i, char in enumerate(compWord):
			chars[i] = char
		
		return len(compWord)
	
"""
time complexity:
- O(n)

space complexity:
- O(1)
"""