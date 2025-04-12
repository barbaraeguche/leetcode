# name: 2. add two numbers
# link: https://leetcode.com/problems/add-two-numbers

# solution #
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		added = str(self.list_to_int(l1) + self.list_to_int(l2))[::-1]
		
		head = ListNode(int(added[0]))
		curr = head
		
		for num in added[1:]:
			curr.next = ListNode(int(num))
			curr = curr.next
		
		return head
	
	@staticmethod
	def list_to_int(list: Optional[ListNode]):
		list_str = ""
		
		while list:
			list_str += str(list.val)
			list = list.next
		
		return int(list_str[::-1])