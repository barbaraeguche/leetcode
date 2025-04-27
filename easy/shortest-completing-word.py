# name: 748. shortest completing word
# link: https://leetcode.com/problems/shortest-completing-word

# solution #
class Solution:
	def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
		arr = []
		licence = "".join(filter(str.isalpha, licensePlate.lower()))
		
		for word in words:
			if len(Counter(licence) - Counter(word)) == 0:
				arr.append(word)
		
		return min(arr, key=len)
	