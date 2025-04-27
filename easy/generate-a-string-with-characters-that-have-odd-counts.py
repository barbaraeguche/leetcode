# name: 1374. generate a string with characters that have odd counts
# link: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts

# solution #
class Solution:
	def generateTheString(self, n: int) -> str:
		if n == 1:
			return "a"
		
		if n % 2 == 0:
			return f"{'a' * (n - 1)}b"
		
		return f"{'a' * (n - 2)}bc"