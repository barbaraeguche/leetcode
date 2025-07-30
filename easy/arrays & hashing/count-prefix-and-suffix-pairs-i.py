# name: 3042. count prefix and suffix pairs i
# link: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i

# solution #
class Solution:
	def countPrefixSuffixPairs(self, words: List[str]) -> int:
		""" we can use brute force since constraints are little """
		
		length, pairCount = len(words), 0
		
		for i in range(length):
			for j in range(i+1, length):
				w1, w2 = words[i], words[j]
				
				if w2.startswith(w1) and w2.endswith(w1):
					pairCount += 1
		
		return pairCount

"""
time complexity:
- O(n^2)

space complexity:
- O(1)
"""