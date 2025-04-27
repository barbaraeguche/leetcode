# name: 804. unique morse code words
# link: https://leetcode.com/problems/unique-morse-code-words

# solution #
class Solution:
	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		encoded = []
		encode_dict = {
			"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
			"e": ".", "f": "..-.", "g": "--.", "h": "....",
			"i": "..", "j": ".---", "k": "-.-", "l": ".-..",
			"m": "--", "n": "-.", "o": "---", "p": ".--.",
			"q": "--.-", "r": ".-.", "s": "...", "t": "-",
			"u": "..-", "v": "...-", "w": ".--", "x": "-..-",
			"y": "-.--", "z": "--.."
		}
		
		def encode_morse(word: str) -> str:
			return "".join(encode_dict[c] for c in word)
		
		for word in words:
			encode = encode_morse(word)
			if encode not in encoded:
				encoded.append(encode)
		
		return len(encoded)
	