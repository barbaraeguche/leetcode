# name: 2269. find the k beauty of a number
# link: https://leetcode.com/problems/find-the-k-beauty-of-a-number

# solution #
class Solution:
	def divisorSubstrings(self, num: int, k: int) -> int:
		numStr, kNum = str(num), 0
		
		for i in range(len(numStr) - k + 1):
			subStr = numStr[i:i + k]
			subInt = int(subStr)
			
			if subInt != 0 and num % subInt == 0:
				kNum += 1
		
		return kNum

"""
time complexity:
- O(n * k); n is the length of the string and k is the int conversion time

space complexity:
- O(n)
"""