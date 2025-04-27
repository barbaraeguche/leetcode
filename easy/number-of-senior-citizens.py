# name: 2678. number of senior citizens
# link: https://leetcode.com/problems/number-of-senior-citizens

# solution #
class Solution:
	def countSeniors(self, details: List[str]) -> int:
		return sum(1 for det in details if int(det[-4:-2]) > 60)
	