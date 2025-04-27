# name: 2130. maximum twin sum of a linked list
# link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

# solution #
class Solution:
	def pairSum(self, head: Optional[ListNode]) -> int:
		stack, slow = self.find_middle(head)
		max_twin = -1
		
		while stack:
			popped = stack.pop()
			value = slow.val
			
			if (popped + value) > max_twin:
				max_twin = popped + value
			
			slow = slow.next
		
		return max_twin
	
	@staticmethod
	def find_middle(head: Optional[ListNode]):
		stack = []
		slow = fast = head
		
		# find the middle node with slow and fast pointers
		while fast and fast.next:
			stack.append(slow.val)
			slow = slow.next
			fast = fast.next.next
		
		return stack, slow
	