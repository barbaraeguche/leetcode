# name: 2788. split strings by separator
# link: https://leetcode.com/problems/split-strings-by-separator

# solution #
class Solution:
	def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
		array = []
		
		for word in words:
			# take the strings with length >= 1
			arr = [w for w in word.split(separator) if w]
			array.extend(arr)
		
		return array
