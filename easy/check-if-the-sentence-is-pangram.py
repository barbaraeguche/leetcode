# name: 1832. check if the sentence is pangram
# link: https://leetcode.com/problems/check-if-the-sentence-is-pangram

# solution #
class Solution:
	def checkIfPangram(self, sentence: str) -> bool:
		letters = set("abcdefghijklmnopqrstuvwxyz")
		counter = set(Counter(sentence).keys())
		
		return len(letters - counter) == 0
	
	def checkIfPangram(self, sentence: str) -> bool:
		return len(set(sentence)) == 26
	