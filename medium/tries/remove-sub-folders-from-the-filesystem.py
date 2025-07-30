# name: 1233. remove sub folders from the filesystem
# link: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.isFolder = False

class Solution:
	def removeSubfolders(self, folder: List[str]) -> List[str]:
		"""
		parent folders are always lexicographically smaller than its subfolders.
		"""
		folder.sort()
		
		nonSubs, root = [], TrieNode()
		
		for fold in folder:
			isSub, node = False, root
			
			# remove initial `/`
			directory = fold[1:].split("/")
			
			for direct in directory:
				if not direct in node.children:
					node.children[direct] = TrieNode()
				node = node.children[direct]
				
				# visiting a sub folder
				if node.isFolder:
					isSub = True
					break
			
			# a main folder
			if not isSub:
				node.isFolder = True
				nonSubs.append(fold)
		
		return nonSubs
	
"""
time complexity:
- O((n * log(n)) + n * m)

space complexity:
- O(n * m)
"""