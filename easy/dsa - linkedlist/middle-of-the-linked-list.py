# name: 876. middle of the linked list
# link: https://leetcode.com/problems/middle-of-the-linked-list

# solution #
class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		slow = fast = head
		
		# find the middle node with slow and fast pointers
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		
		return slow