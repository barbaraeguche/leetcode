# name: 2269. find the k beauty of a number
# link: https://leetcode.com/problems/find-the-k-beauty-of-a-number

# solution #
class Solution:
	def divisorSubstrings(self, num: int, k: int) -> int:
		count, string = 0, str(num)
		
		# split into blocks
		array = [string[i:i+k] for i in range(len(string))]
		
		for chunk in array:
			if len(chunk) == k:
				n = int(chunk)
				
				if n > 0 and num % n == 0:
					count += 1
		
		return count
