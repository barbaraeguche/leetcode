# name: 206. reverse-linked-list
# link: https://leetcode.com/problems/reverse-linked-list

# solution #
class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head: return None
		if not head.next: return head
		
		prev, curr = None, head
		temp = curr.next
		
		while curr.next:
			curr.next = prev
			prev = curr
			curr = temp
			temp = curr.next
		
		curr.next = prev
		return curr
	