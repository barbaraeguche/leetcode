# name: 1935. maximum number of words you can type
# link: https://leetcode.com/problems/maximum-number-of-words-you-can-type

# solution #
class Solution:
	def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
		arr = []
		
		for word in text.split():
			if len(set(word) & set(brokenLetters)) == 0:
				arr.append(word)
		
		return len(arr)