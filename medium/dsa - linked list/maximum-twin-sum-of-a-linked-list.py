# name: 2130. maximum twin sum of a linked list
# link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

# solution #
class Solution:
	def pairSum(self, head: Optional[ListNode]) -> int:
		stack, slow = self.getMiddle(head)
		maxTwin = -1
		
		while stack:
			maxTwin = max(maxTwin, stack.pop() + slow.val)
			slow = slow.next
		
		return maxTwin
	
	def getMiddle(self, head: Optional[ListNode]):
		slow = fast = head
		stack = []
	
		# find the middle node with slow and fast pointers
		while fast and fast.next:
			stack.append(slow.val)
			slow = slow.next
			fast = fast.next.next
		
		return stack, slow

"""
time complexity:
- O(n)

space complexity:
- O(n // 2)
"""