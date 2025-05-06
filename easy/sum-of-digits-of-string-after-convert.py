# name: 1945. sum of digits of string after convert
# link: https://leetcode.com/problems/sum-of-digits-of-string-after-convert

# solution #
class Solution:
	def getLucky(self, s: str, k: int) -> int:
		base, string = ord('a') - 1, ""
		
		for char in s:
			string += str(ord(char) - base)
		
		for _ in range(k):
			string = str(sum(int(num) for num in string))
		
		return int(string)
