# name: 3014. minimum number of pushes to type word i
# link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i

# solution #
class Solution:
	def minimumPushes(self, word: str) -> int:
		pushes = 0
		
		# can be placed in 8 places
		quot, rem = divmod(len(word), 8)
		
		# presses for each i
		for i in range(quot):
			pushes += (i + 1) * 8
		
		# remaining presses
		pushes += (quot + 1) * rem
		
		return pushes

"""
time complexity:
- O(quot)

space complexity:
- O(1)
"""