# name: 205. isomorphic strings
# link: https://leetcode.com/problems/isomorphic-strings

# solution #
class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		zip_dict = {}
		
		for k, v in zip(s, t):
			if v in zip_dict.values():
				key_with_v = next(key for key, val in zip_dict.items() if val == v)
				if key_with_v != k:
					return False
			
			elif k in zip_dict and zip_dict[k] != v:
				return False
			
			zip_dict |= { k: v }
		
		return True
