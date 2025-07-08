# name: 1684. count the number of consistent strings
# link: https://leetcode.com/problems/count-the-number-of-consistent-strings

# solution #
class Solution:
	def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
		consistent, countAllowed = 0, Counter(allowed)
		
		for word in words:
			valid = True
			
			for char in word:
				if char not in countAllowed:
					valid = False
					break
			
			consistent += 1 if valid else 0
		
		return consistent

"""
time complexity:
- O(n * m); n is the length of the array, m is length of each word

space complexity:
- O(1)
"""