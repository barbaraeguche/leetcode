# name: 2942. find words containing character
# link: https://leetcode.com/problems/find-words-containing-character

# solution #
class Solution:
	def findWordsContaining(self, words: List[str], x: str) -> List[int]:
		for i, word in enumerate(words):
			if x in word:
				words[i] = i
		
		return [num for num in words if str(num).isdigit()]
