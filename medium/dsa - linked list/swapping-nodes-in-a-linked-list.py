# name: 1721. swapping nodes in a linked list
# link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list

# solution #
class Solution:
	def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		node_a = head
		for _ in range(k - 1):
			node_a = node_a.next
		
		node_b, temp = head, node_a
		
		while temp.next:
			temp = temp.next
			node_b = node_b.next
		
		node_a.val, node_b.val = node_b.val, node_a.val
		
		return head
