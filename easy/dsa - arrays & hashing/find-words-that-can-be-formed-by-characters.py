# name: 1160. find words that can be formed by characters
# link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

# solution #
class Solution:
	def countCharacters(self, words: List[str], chars: str) -> int:
		count, charsMap = 0, defaultdict(int)
		
		# store count of characters in chars
		for char in chars:
			charsMap[char] += 1
		
		# check if it can be formed
		for word in words:
			for char in set(word):
				# cannot be formed
				if not char in charsMap:
					break
				
				# way too many letters
				if not word.count(char) <= charsMap[char]:
					break
			
			else:
				count += len(word)
		
		return count
