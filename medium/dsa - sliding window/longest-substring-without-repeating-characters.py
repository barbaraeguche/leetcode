# name: 3. longest substring without repeating characters
# link: https://leetcode.com/problems/longest-substring-without-repeating-characters

# solution #
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		seen = {}
		left = maxLen = 0
		
		for right, char in enumerate(s):
			if char in seen and seen[char] >= left:
				left = seen[char] + 1  # shrink the window
			
			seen[char] = right  # update the latest index
			maxLen = max(maxLen, right - left + 1)
		
		return maxLen

"""
time complexity:
- O(n)

space complexity:
- O(k); k is the number of unique characters
"""