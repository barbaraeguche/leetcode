# name: 1455. check if a word occurs as a prefix of any word in a sentence
# link: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

# solution #
class Solution:
	def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
		length = len(searchWord)
		
		for i, word in enumerate(sentence.split()):
			if length <= len(word) and word[:length] == searchWord:
				return i + 1
		
		return -1
