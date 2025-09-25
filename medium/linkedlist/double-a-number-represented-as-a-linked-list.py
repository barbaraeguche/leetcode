# name: 2816. double a number represented as a linked list
# link: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list

# solution #
class Solution:
	def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
		def doubleNum(root):
			if not root:
				return 0, None
			
			num, _ = doubleNum(root.next)
			carry, val = divmod(root.val * 2 + num, 10)
			
			root.val = val
			return carry, root
		
		carry, node = doubleNum(head)
		
		if carry != 0:
			node = ListNode(carry, node)
		
		return node

"""
time complexity:
- O(n)

space complexity:
- O(n); n being the call stack
"""