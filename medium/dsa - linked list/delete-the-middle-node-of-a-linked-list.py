# name: 2095. delete the middle node of a linked list
# link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# solution #
class Solution:
	def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# if there's only one node, delete it and return None
		if not head.next:
			return None
		
		prev = None
		slow = fast = head
		
		# find the middle node with slow and fast pointers
		while fast and fast.next:
			prev = slow
			slow = slow.next
			fast = fast.next.next
		
		# delete the middle node
		if prev:
			prev.next = slow.next
		
		return head
	