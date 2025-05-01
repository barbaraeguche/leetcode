# name: 49. group anagrams
# link: https://leetcode.com/problems/group-anagrams

# solution #
class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		hashm = {}
		
		for word in strs:
			# sort the string, and use that as key
			string = "".join(sorted(word))
			
			# store the word in an array
			hashm.setdefault(string, []).append(word)
		
		return [v for _, v in hashm.items()]
	