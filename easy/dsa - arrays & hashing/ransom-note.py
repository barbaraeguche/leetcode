# name: 383. ransom note
# link: https://leetcode.com/problems/ransom-note

# solution #
class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		magazineCount = defaultdict(int)
		
		# char-freq pairs
		for char in magazine:
			magazineCount[char] += 1
		
		for char in ransomNote:
			# cannot be constructed
			if not char in magazineCount:
				return False
			
			# reduce the frequency of char
			magazineCount[char] -= 1
			
			# all chars have been exhausted
			if magazineCount[char] == 0:
				del magazineCount[char]
		
		return True

"""
time complexity:
- O(n + m); n is the length of magazine, m is the length of ransomNote

space complexity:
- O(1)
"""