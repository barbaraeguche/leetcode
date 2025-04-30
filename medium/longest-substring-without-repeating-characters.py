# name: 3. longest substring without repeating characters
# link: https://leetcode.com/problems/longest-substring-without-repeating-characters

# solution #
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		string = ""
		seen = set()
		
		for i, char in enumerate(s):
			if char in string:
				seen.add(string)
				idx = string.index(char) + 1
				
				string = string[idx:] + char
			else:
				string += char
			
			if i == len(s) - 1:
				seen.add(string)
		
		return 0 if len(seen) == 0 else len(max(seen, key=len))
	
	def lengthOfLongestSubstring(self, s: str) -> int:
		count, string = 0, ""
	
		for i, char in enumerate(s):
			if char in string:
				# keep track of the length
				count = max(count, len(string))
				
				# find the index of the character
				idx = string.index(char)
				# remove it and append new character
				string = string[idx+1:] + char
			else:
				string += char
			
			# if the last character
			if i == len(s) - 1:
				count = max(count, len(string))
		
		return count
	