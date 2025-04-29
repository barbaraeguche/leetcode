# name: 2586. count the number of vowel strings in range
# link: https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range

# solution #
class Solution:
	def vowelStrings(self, words: List[str], left: int, right: int) -> int:
		words = words[left:right + 1]
		
		count, vowels = 0, "aeiou"
		
		for word in words:
			if word[0] in vowels and word[-1] in vowels:
				count += 1
		
		return count
