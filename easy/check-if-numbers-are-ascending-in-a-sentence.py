# name: 2042. check if numbers are ascending in a sentence
# link: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence

# solution #
class Solution:
	def areNumbersAscending(self, s: str) -> bool:
		filtered = re.findall(r'\d+', s)
		ordered = list(map(int, filtered))
		
		for i in range(len(ordered) - 1):
			if not ordered[i] < ordered[i+1]:
				return False
		
		return True
	