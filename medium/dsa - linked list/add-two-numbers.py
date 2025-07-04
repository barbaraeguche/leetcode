# name: 2. add two numbers
# link: https://leetcode.com/problems/add-two-numbers

# solution #
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		return self.addNums(l1, l2, 0)
	
	@staticmethod
	def addNums(l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
		# if no node and carry-over is empty
		if not l1 and not l2 and carry == 0:
			return None
		
		# get the values
		v1 = l1.val if l1 else 0
		v2 = l2.val if l2 else 0
		
		# perform arithmetic
		rem, quot = divmod(v1 + v2 + carry, 10)
		
		# calculate the next value
		node = Solution.addNums(
			l1.next if l1 else None,
			l2.next if l2 else None,
			rem
		)
		
		return ListNode(quot, node)
