# name: 24. swap nodes in pairs
# link: https://leetcode.com/problems/swap-nodes-in-pairs

# solution #
class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		def swapNodes(root):
			if not root:
				return None
			if not root.next:
				return root
			
			prev, curr = root, root.next
			
			# node a -> node b.next
			prev.next = swapNodes(curr.next)
			# node b -> node a
			curr.next = prev
			
			# return the newly reversed node
			return curr
		
		return swapNodes(head)

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""