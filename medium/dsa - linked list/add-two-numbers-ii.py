# name: 445. add two numbers ii
# link: https://leetcode.com/problems/add-two-numbers-ii

# solution #
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		def printList(link: Optional[ListNode]) -> int:
			num = ""
			
			while link:
				num += str(link.val)
				link = link.next
			
			return int(num)
		
		# get the summation
		total = str(printList(l1) + printList(l2))
		
		head = ListNode(int(total[0]))
		curr = head
		
		for num in total[1:]:
			curr.next = ListNode(int(num))
			curr = curr.next
		
		return head
	