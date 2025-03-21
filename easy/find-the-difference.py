# name: 389. find the difference
# link: https://leetcode.com/problems/find-the-difference

# solution #
class Solution:
	def findTheDifference(self, s: str, t: str) -> str:
		return (Counter(t) - Counter(s)).most_common()[0][0]