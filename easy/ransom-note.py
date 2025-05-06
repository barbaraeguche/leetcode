# name: 383. ransom note
# link: https://leetcode.com/problems/ransom-note

# solution #
class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		ransom_counter = Counter(ransomNote)
		ransom_mag = Counter(magazine)
		
		return len(ransom_counter - ransom_mag) == 0
	