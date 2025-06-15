# name: 2399. check distances between same letters
# link: https://leetcode.com/problems/check-distances-between-same-letters

# solution #
class Solution:
	def checkDistances(self, s: str, distance: List[int]) -> bool:
		base, distHash = ord('a'), {}
		
		for i, char in enumerate(s):
			if char in distHash:
				dist = i - distHash[char] - 1
				
				# validate distance
				if distance[ord(char) - base] != dist:
					return False
			else:
				distHash[char] = i
		
		return True

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""