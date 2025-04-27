# name: 2138. divide a string into groups of size k
# link: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k

# solution #
class Solution:
	def divideString(self, s: str, k: int, fill: str) -> List[str]:
		arr = [s[i:i+k] for i in range(0, len(s), k)]
		
		if len(arr[-1]) != k:
			arr[-1] = arr[-1].ljust(k, fill)
		
		return arr
	