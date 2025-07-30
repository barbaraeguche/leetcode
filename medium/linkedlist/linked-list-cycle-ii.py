# name: 142. linked list cycle ii
# link: https://leetcode.com/problems/linked-list-cycle-ii

# solution #
class Solution:
	def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
		slow = fast = head
		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			
			if slow == fast:
				break
		
		# no cycle
		if not fast or not fast.next:
			return None
		
		fast = head
		
		while slow != fast:
			slow = slow.next
			fast = fast.next
		
		return slow

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""