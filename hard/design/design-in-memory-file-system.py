# name: 588. design in memory file system
# link: https://leetcode.com/problems/design-in-memory-file-system

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.contents = ""

class FileSystem:
	
	def __init__(self):
		self.root = TrieNode()
	
	def ls(self, path: str) -> List[str]:
		node = self.mkdirHelper(path, False)
		
		folderContents = []
		
		# path is a file path
		if node.contents != "":
			folderContents.append(path.split("/")[-1])
		
		# path is a directory
		if node.children:
			folderContents.extend(node.children.keys())
		
		return list(sorted(folderContents))
	
	def mkdir(self, path: str) -> None:
		_ = self.mkdirHelper(path)
	
	def addContentToFile(self, filePath: str, content: str) -> None:
		node = self.mkdirHelper(filePath)
		
		# add content to file
		node.contents += content
	
	def readContentFromFile(self, filePath: str) -> str:
		node = self.mkdirHelper(filePath)
		return node.contents
	
	def mkdirHelper(self, path: str, isMkdir: bool = True):
		"""
		isMkdir is False when calling the `ls` method to prevent
		a child creation
		"""
		node = self.root
		
		# get each independent directory
		directory = ["/"] + [p for p in path.split("/") if p]
		
		for direct in directory:
			if isMkdir and not direct in node.children:
				node.children[direct] = TrieNode()
			
			# the `ls` method was called
			if not direct in node.children:
				break
			
			node = node.children[direct]
		
		return node

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""