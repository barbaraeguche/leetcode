# name: 203. remove linked list elements
# link: https://leetcode.com/problems/remove-linked-list-elements

# solution #
class Solution:
	def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
		current = head
		
		while current and current.next:
			while current.next and current.next.val == val:
				current.next = current.next.next
			
			current = current.next
		
		if head and head.val == val:
			head = head.next
		
		return head