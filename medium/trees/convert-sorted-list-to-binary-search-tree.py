# name: 109. convert sorted list to binary search tree
# link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# solution #
class Solution:
	def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
		# empty list
		if not head:
			return head
		
		# middle of the current list
		mid = self.getMiddle(head)
		# the middle becomes the root
		root = TreeNode(mid.val)
		
		# only one node left in the tree
		if head == mid:
			return root
		
		root.left = self.sortedListToBST(head)
		root.right = self.sortedListToBST(mid.next)
		
		return root
	
	def getMiddle(self, node):
		prev = None
		slow = fast = node
		
		while fast and fast.next:
			prev = slow
			slow = slow.next
			fast = fast.next.next
		
		# disconnect the left from the mid
		if prev:
			prev.next = None
		
		return slow

"""
time complexity:
- O(n * log(n))

space complexity:
- O(log(n))
"""