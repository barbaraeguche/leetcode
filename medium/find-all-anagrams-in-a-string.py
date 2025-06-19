# name: 438. find all anagrams in a string
# link: https://leetcode.com/problems/find-all-anagrams-in-a-string

# solution #
class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		n, m = len(s), len(p)
		
		# cannot be a permutation
		if n < m:
			return []
		
		pCount = Counter(p)
		windowCount = Counter(s[:m])
		
		result = []
		
		# first n characters are equal
		if pCount == windowCount:
			result.append(0)
		
		for i in range(m, n):
			# remove leftmost char of the window
			leftChar = s[i - m]
			windowCount[leftChar] -= 1
			
			if windowCount == 0:
				del windowCount[leftChar]
			
			# add new char to the window
			rightChar = s[i]
			windowCount[rightChar] += 1
			
			if windowCount == pCount:
				result.append(i - m + 1)
		
		return result

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""