# name: 21. merge two sorted lists
# link: https://leetcode.com/problems/merge-two-sorted-lists

# solution #
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if not list1: return list2
		if not list2: return list1
		
		# choose the starting node
		head = ListNode(0)
		current = head
		
		# merge the lists
		while list1 and list2:
			if list1.val < list2.val:
				current.next = list1
				list1 = list1.next
			else:
				current.next = list2
				list2 = list2.next
			
			current = current.next
		
		# attach the remaining nodes
		current.next = list1 if list1 else list2
		
		return head.next
	