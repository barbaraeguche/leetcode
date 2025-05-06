# name: 83. remove duplicates from sorted list
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-list

# solution #
class Solution:
	def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head is None:
			return None
		
		if not head.next:
			return head
		
		seen = set([head.val])
		current = head
		
		while current.next:
			if current.next.val in seen:
				current.next = current.next.next
			else:
				# add val to set
				seen.add(current.next.val)
				current = current.next
		
		return head
	