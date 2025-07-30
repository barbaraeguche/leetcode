# name: 3043. find the length of the longest common prefix
# link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}

class Solution:
	def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
		longest, root = 0, TrieNode()
		
		# add arr1 elements to trie
		for num in arr1:
			node = root
			
			for digit in str(num):
				if not digit in node.children:
					node.children[digit] = TrieNode()
				node = node.children[digit]
		
		# find the arr2 numbers in trie
		for num in arr2:
			length, node = 0, root
			
			for digit in str(num):
				# not a common prefix
				if not digit in node.children:
					break
				
				length += 1
				node = node.children[digit]
			
			# take the max length
			longest = max(longest, length)
		
		return longest

"""
time complexity:
- O((n1 + n2) * d); n$ is the length of the array, d is the average number of digits per number

space complexity:
- O(n1 * d)
"""