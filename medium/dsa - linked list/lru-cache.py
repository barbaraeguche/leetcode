# name: 146. lru cache
# link: https://leetcode.com/problems/lru-cache

# solution #
"""
when either get (and key exist) or put is called, move the node
to the end of the list as it becomes the most recently used
"""

class Node():
	def __init__(self, key: int, value: int):
		self.key = key
		self.value = value
		# use doubly linked lists
		self.prev = self.next = None

class LRUCache:
	
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.cache = {}
		
		# dummy left-right nodes
		self.left, self.right = Node(0, 0), Node(0, 0)
		# connect them
		self.left.next, self.right.prev = self.right, self.left
	
	def get(self, key: int) -> int:
		if key in self.cache:
			node = self.cache[key]
			
			# make most recently used
			self.remove(node)
			self.insert(node)
			
			return node.value
		
		return -1
	
	def put(self, key: int, value: int) -> None:
		if key in self.cache:
			self.remove(self.cache[key])
		
		node = Node(key, value)
		
		# add to cache and list
		self.cache[key] = node
		self.insert(node)
		
		# cache must be in range of capacity
		if len(self.cache) > self.capacity:
			lru = self.left.next
			
			# remove from cache and list
			self.remove(lru)
			del self.cache[lru.key]
	
	def insert(self, node: Node) -> None:
		penultimate, last = self.right.prev, self.right
		
		# connect nodes
		penultimate.next = last.prev = node
		node.prev, node.next = penultimate, last
	
	def remove(self, node: Node) -> None:
		prev, nxt = node.prev, node.next
		prev.next, nxt.prev = nxt, prev
		