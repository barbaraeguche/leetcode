# name: 824. goat latin
# link: https://leetcode.com/problems/goat-latin

# solution #
class Solution:
	def toGoatLatin(self, sentence: str) -> str:
		string = ""
		
		for i, word in enumerate(sentence.split()):
			first = word[0]
			
			if first.lower() in "aeiou":
				string += f"{word}ma{'a' * (i + 1)} "
			else:
				string += f"{word[1:]}{first}ma{'a' * (i + 1)} "
		
		return string.strip()