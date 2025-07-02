# name: 1166. design file system
# link: https://leetcode.com/problems/design-file-system

# solution #
class FileSystem:
	
	def __init__(self):
		self.fileMap = {}
	
	def createPath(self, path: str, value: int) -> bool:
		# path already exists
		if path in self.fileMap:
			return False
		
		# get rid of empty strings
		paths = [p for p in path.split("/") if p][:-1]
		
		# parent directories
		if len(paths):
			string = ""
			
			for p in paths:
				string += f"/{p}"
				
				# parent directory does not exist in hash map
				if not string in self.fileMap:
					return False
		
		# add path-value to map
		self.fileMap[path] = value
		return True
	
	def get(self, path: str) -> int:
		return self.fileMap.get(path, -1)

"""
time complexity:
- O(n)

space complexity:
- O(p * l); p is the number of paths, l is the average length of each path string
"""