# name: 541. reverse string ii
# link: https://leetcode.com/problems/reverse-string-ii

# solution #
class Solution:
	def reverseStr(self, s: str, k: int) -> str:
		# split the string into chunks of size 2k
		chunks = [s[i:i + (2 * k)] for i in range(0, len(s), 2 * k)]
		result = []
		
		# process all chunks except the last
		for chunk in chunks[:-1]:
			result.append(chunk[:k][::-1] + chunk[k:])
		
		# handle the last chunk
		last_chunk = chunks[-1]
		
		if len(last_chunk) < k:
			result.append(last_chunk[::-1])
		elif k <= len(last_chunk) <= 2 * k:
			result.append(last_chunk[:k][::-1] + last_chunk[k:])
		
		return "".join(result)