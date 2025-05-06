# name: 1805. number of different integers in a string
# link: https://leetcode.com/problems/number-of-different-integers-in-a-string

# solution #
class Solution:
	def numDifferentIntegers(self, word: str) -> int:
		nums = list(map(int, re.findall(r'\d+', word)))
		return len(set(nums))
	