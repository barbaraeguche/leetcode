# name: 23. merge k sorted lists
# link: https://leetcode.com/problems/merge-k-sorted-lists

# solution #
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		for i in range(1, len(lists)):
			lists[i] = self.mergeList(lists[i-1], lists[i])
		
		return lists[-1] if lists else None
	
	@staticmethod
	def mergeList(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		head = ListNode(0)
		curr = head
		
		# merge the list
		while l1 and l2:
			if l1.val < l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			
			curr = curr.next
		
		# add the remaining nodes
		curr.next = l1 if l1 else l2
		
		# .next because we started with a random value
		return head.next
