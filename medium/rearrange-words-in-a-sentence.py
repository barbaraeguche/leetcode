# name: 1451. rearrange words in a sentence
# link: https://leetcode.com/problems/rearrange-words-in-a-sentence

# solution #
class Solution:
	def arrangeWords(self, text: str) -> str:
		hashm: Dict[int, List[str]] = {}
		string = ""
		
		# store in the map with length as its key
		for word in text.split():
			hashm.setdefault(len(word), []).append(word)
		
		# sort the map based on key asc
		hashm = dict(sorted(hashm.items(), key=lambda x: x[0]))
		
		# merge into string
		for _, v in hashm.items():
			string += f"{' '.join(v)} "
		
		# remove last space
		string = string.strip()
		
		return string[0].upper() + string[1:].lower()
	