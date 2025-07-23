# name: 3304. find the k th character in string game i
# link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i

# solution #
class Solution:
	def kthCharacter(self, k: int) -> str:
		base, charArr = ord("a"), ["a"]
		
		while len(charArr) <= k:
			for i in range(len(charArr)):
				char = charArr[i]
				
				# get the next alphabet
				nextChar = ord(char) + 1
				
				# normalize the boundaries
				normChar = (nextChar - base) % 26
				
				# append the next alphabet
				charArr.append(chr(base + normChar))
		
		return charArr[k-1]
	
"""
time complexity:
- O(k)

space complexity:
- O(k)
"""