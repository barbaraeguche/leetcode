# name: 141. linked list cycle
# link: https://leetcode.com/problems/linked-list-cycle

# solution #
class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		slow = fast = head
		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			
			if slow == fast:
				return True
		
		return False