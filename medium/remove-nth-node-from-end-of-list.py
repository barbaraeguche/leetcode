# name: 19. remove nth node from end of list
# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list

# solution #
class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		slow = fast = head
		
		# move this n steps
		for _ in range(n):
			fast = fast.next
		
		if not fast:
			return head.next
		
		# update until fast.next is None
		while fast.next:
			slow = slow.next
			fast = fast.next
		
		# remove the node
		slow.next = slow.next.next
		
		return head
	