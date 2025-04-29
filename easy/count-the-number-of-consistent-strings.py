# name: 1684. count the number of consistent strings
# link: https://leetcode.com/problems/count-the-number-of-consistent-strings

# solution #
class Solution:
	def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
		count = 0
		counter_allowed = Counter(allowed)
		
		for word in words:
			if len(Counter(set(word)) - counter_allowed) == 0:
				count += 1
		
		return count
	