# name: 2744. find maximum number of string pairs
# link: https://leetcode.com/problems/find-maximum-number-of-string-pairs

# solution #
class Solution:
	def maximumNumberOfStringPairs(self, words: List[str]) -> int:
		base, pairMap = ord('a'), defaultdict(int)
		
		for word in words:
			# character array
			ordArr = [0] * 26
			
			# at most 2 characters
			for i in range(2):
				ordArr[ord(word[i]) - base] += 1
			
			# use the ord array as key
			pairMap[tuple(ordArr)] += 1
		
		# only ones that have a pair
		return sum(1 for _, v in pairMap.items() if v == 2)

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""