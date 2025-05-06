# name: 1773. count items matching a rule
# link: https://leetcode.com/problems/count-items-matching-a-rule

# solution #
class Solution:
	def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
		count = 0
		hashm = { "type": 0, "color": 1, "name": 2 }
		
		for item in items:
			if item[hashm[ruleKey]] == ruleValue:
				count += 1
		
		return count
	