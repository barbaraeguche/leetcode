# name: 242. valid anagram
# link: https://leetcode.com/problems/valid-anagram

# solution #
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		sMap, tMap = defaultdict(int), defaultdict(int)
	
		for char in s:
			sMap[char] = sMap.get(char, 0) + 1
		for char in t:
			# must have same characters in s
			if not char in sMap:
				return False
			tMap[char] = tMap.get(char, 0) + 1
		
		# since both contain the same characters, loop through s
		# and return False if the counts differ
		for char in sMap.keys():
			if sMap[char] != tMap[char]:
				return False
		
		return True

"""
time complexity:
- O(n+m); n in the length of s and m is the length of t

space complexity:
- O(1)
"""