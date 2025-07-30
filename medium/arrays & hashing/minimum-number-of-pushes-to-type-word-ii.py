# name: 3016. minimum number of pushes to type word ii
# link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii

# solution #
class Solution:
	def minimumPushes(self, word: str) -> int:
		pushMap = Counter(word)
		
		"""
		sort by count in reversed order
		higher frequencies should have minimal pushes
		"""
		pushMap = dict(sorted(pushMap.items(), key=lambda x: -x[1]))
		
		idx = pushes = 0
		
		for _, freq in pushMap.items():
			# can be placed in 8 places
			quot, rem = divmod(idx, 8)
			idx += 1
			
			# presses for each i
			pushes += (quot + 1) * freq
		
		return pushes

"""
time complexity:
- O(n * log(n))

space complexity:
- O(1)
"""