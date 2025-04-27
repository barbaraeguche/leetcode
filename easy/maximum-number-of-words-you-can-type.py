# name: 1935. maximum number of words you can type
# link: https://leetcode.com/problems/maximum-number-of-words-you-can-type

# solution #
class Solution:
	def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
		arr = []
		broken = set(brokenLetters)
		
		for word in text.split():
			if len(set(word) & broken) == 0:
				arr.append(word)
		
		return len(arr)
	