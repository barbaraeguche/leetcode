# name: 744. find smallest letter greater than target
# link: https://leetcode.com/problems/find-smallest-letter-greater-than-target

# solution #
class Solution:
	def nextGreatestLetter(self, letters: List[str], target: str) -> str:
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		idx = alphabets.index(target)
		
		for lett in alphabets[idx + 1:]:
			if lett in letters:
				return lett
		
		return letters[0]
