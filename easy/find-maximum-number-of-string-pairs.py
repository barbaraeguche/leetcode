# name: 2744. find maximum number of string pairs
# link: https://leetcode.com/problems/find-maximum-number-of-string-pairs

# solution #
class Solution:
	def maximumNumberOfStringPairs(self, words: List[str]) -> int:
		hashm = {}
		
		for word in words:
			# sort the string and store as the key
			string = "".join(sorted(word))
			
			# store the count as the value
			if string in hashm:
				hashm[string] += 1
			else:
				hashm |= { string: 1 }
		
		# find the count where the value is even
		count = sum(1 for _,v in hashm.items() if v % 2 == 0)
		
		return count
