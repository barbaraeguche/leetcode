# name: 557. reverse words in a string iii
# link: https://leetcode.com/problems/reverse-words-in-a-string-iii

# solution #
class Solution:
	def reverseWords(self, s: str) -> str:
		return " ".join(self.swap(word) for word in s.split())
	
	@staticmethod
	def swap(word: str) -> str:
		arr = list(word)
		L, R = 0, len(word) - 1
		
		while L < R:
			arr[L], arr[R] = arr[R], arr[L]
			L += 1
			R -= 1
		
		return "".join(arr)
