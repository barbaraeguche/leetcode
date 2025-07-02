# name: 3330. find the original typed string i
# link: https://leetcode.com/problems/find-the-original-typed-string-i

# solution #
class Solution:
	def possibleStringCount(self, word: str) -> int:
		current, count, right = word[0], 1, 1
		
		for char in word[1:]:
			if char == current:
				# extend running length
				right += 1
			else:
				# running length of current character
				count += right - 1 if right > 1 else 0
				
				# reset right pointer; update the character
				right = 1
				current = char
		
		# for the last running character
		count += right - 1 if right > 1 else 0
		
		return count

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""