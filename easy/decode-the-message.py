# name: 2325. decode the message
# link: https://leetcode.com/problems/decode-the-message

# solution #
class Solution:
	def decodeMessage(self, key: str, message: str) -> str:
		idx, base = 0, ord('a')
		mapping = {}
		
		# find unique characters in key
		for char in key:
			if char.isalpha() and char not in mapping:
				mapping[char] = chr(base + idx)
				idx += 1
		
		decoded = []
	
		# decode the message
		for char in message:
			decoded.append(char if char == " " else mapping[char])
			
		return "".join(decoded)

"""
time complexity:
- O(n + m); n is the length of the key, m is the length of the message

space complexity:
- O(1)
"""