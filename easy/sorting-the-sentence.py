# name: 1859. sorting the sentence
# link: https://leetcode.com/problems/sorting-the-sentence

# solution #
class Solution:
	def sortSentence(self, s: str) -> str:
		splitted = s.split()
		arr = [""] * len(splitted)
		
		for _, text in enumerate(splitted):
			arr[int(text[-1]) - 1] = text[:-1]
		
		return " ".join(arr)
	