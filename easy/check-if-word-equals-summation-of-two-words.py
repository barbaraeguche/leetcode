# name: 1880. check if word equals summation of two words
# link: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words

# solution #
class Solution:
	def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
		def num_value(word: str) -> int:
			arr = []
			for w in word:
				arr.append(str(ord(w) - ord('a')))
			
			return int("".join(arr))
		
		return (num_value(firstWord) + num_value(secondWord)) == num_value(targetWord)
	