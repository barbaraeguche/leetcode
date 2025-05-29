# name: 271. encode and decode strings
# link: https://leetcode.com/problems/encode-and-decode-strings

# solution #
class Codec:
	def encode(self, strs: List[str]) -> str:
		"""Encodes a list of strings to a single string.
		"""
		string = ""
		
		for word in strs:
			string += f"{len(word)}#{word}"
		
		return string
	
	def decode(self, s: str) -> List[str]:
		"""Decodes a single string to a list of strings.
		"""
		result = []
		i, temp = 0, ""
		
		while len(s):
			# while not found the delimiter
			while not temp.endswith('#'):
				temp += s[i]
				i += 1
			
			# length of each word
			length = int(temp[:-1])
			
			# append to array
			result.append(s[i:i + length])
			
			# remove word from string
			s = s[i + length:]
			
			# clear variables
			i, temp = 0, ""
		
		return result
