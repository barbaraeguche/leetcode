# name: 49. group anagrams
# link: https://leetcode.com/problems/group-anagrams

# solution #
class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		base, hashMap = ord('a'), defaultdict(list)
		
		for word in strs:
			# for all possible characters
			charArr = [0] * 26
			
			for char in word:
				charArr[ord(char) - base] += 1
			
			# store in the map using the ascii array value as key
			hashMap[tuple(charArr)].append(word)
		
		# return all values
		return list(hashMap.values())
	