# name: 205. isomorphic strings
# link: https://leetcode.com/problems/isomorphic-strings

# solution #
class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		zip_dict = {}
		
		for k, v in zip(s, t):
			if k in zip_dict and zip_dict[k] != v:
				return False
			
			elif v in zip_dict.values():
				key_with_v = next((key for key, val in zip_dict.items() if v == val), None)
				if key_with_v != k:
					return False
			
			zip_dict |= { k: v }
		
		return True
