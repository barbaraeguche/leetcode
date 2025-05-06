# name: 2325. decode the message
# link: https://leetcode.com/problems/decode-the-message

# solution #
class Solution:
	def decodeMessage(self, key: str, message: str) -> str:
		base, string = ord('a'), ""
		idx = 0
		
		hashm = {}
		
		# find unique characters in key
		for char in key:
			if char not in hashm.keys() and char.isalpha():
				hashm |= { char: chr(base + idx) }
				idx += 1
		
		# decode the message
		for char in message:
			if char == " ":
				string += char
			else:
				string += hashm[char]
		
		return string
