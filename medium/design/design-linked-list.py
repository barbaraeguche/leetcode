# name: 707. design linked list
# link: https://leetcode.com/problems/design-linked-list

# solution #
class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class MyLinkedList:
	
	def __init__(self):
		self.head = Node(-1)
		self.tail = self.head
	
	def get(self, index: int) -> int:
		idx, curr = 0, self.head.next
		
		while curr:
			if idx == index:
				return curr.val
			
			idx += 1
			curr = curr.next
		
		return -1  # index out of bound
	
	def addAtHead(self, val: int) -> None:
		newHead = Node(val)
		
		# add at head
		newHead.next = self.head.next
		self.head.next = newHead
		
		# if the first node in the list
		if not newHead.next:
			self.tail = newHead
	
	def addAtTail(self, val: int) -> None:
		newTail = Node(val)
		
		self.tail.next = newTail
		self.tail = newTail
	
	def addAtIndex(self, index: int, val: int) -> None:
		idx, curr = 0, self.head
		
		while idx < index and curr:
			idx += 1
			curr = curr.next
		
		if curr:
			if curr.next:
				node = Node(val)
				
				# add to list
				node.next = curr.next
				curr.next = node
			
			# append to tail
			else:
				self.addAtTail(val)
	
	def deleteAtIndex(self, index: int) -> None:
		idx, curr = 0, self.head
		
		while idx < index and curr:
			idx += 1
			curr = curr.next
		
		if curr and curr.next:
			# set tail to curr if deleting the last node in the list
			if self.tail == curr.next:
				self.tail = curr
			
			# delete the node
			curr.next = curr.next.next
