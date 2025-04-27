# name: 500. keyboard row
# link: https://leetcode.com/problems/keyboard-row

# solution #
class Solution:
	def findWords(self, words: List[str]) -> List[str]:
		arr = []
		row_1 = set("qwertyuiop")
		row_2 = set("asdfghjkl")
		row_3 = set("zxcvbnm")
		
		def is_one_row(word: str) -> bool:
			word_set = set(word.lower())
			return sum(1 for row in (row_1, row_2, row_3) if word_set & row)
		
		for word in words:
			if is_one_row(word) == 1:
				arr.append(word)
		
		return arr
	